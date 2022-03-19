from dirtyscatter.config import config
from dirtyscatter.db.orm import User, History
from dirtyscatter.scraper.ChromeBrowser import ChromeBrowser
from time import sleep
import time


class ScatterScraper:

    def __init__(self, leaderboard_url, table_x_path, next_page_button_x_path, total_shown_x_path,
                 chromedriver_path=None):
        self.browser = ChromeBrowser(chromedriver_path, headless=True)
        self.leaderboard_url = leaderboard_url
        self.next_page_button_x_path = next_page_button_x_path
        self.table_x_path = table_x_path
        self.total_shown_x_path = total_shown_x_path

    def get_all_current_user(self):
        with self.browser as session:
            session.get(self.leaderboard_url)
            sleep(2)
            return self.__extract_all_current_user(session)

    def __is_last_page(self, session):
        element = session.find_elements_by_xpath(self.total_shown_x_path)[0]
        text = element.text
        total_users = text.split(' ')[-1]
        displayed_to = text.split(' ')[2]
        return int(displayed_to) >= int(total_users)

    def __next_page(self, session):
        if self.__is_last_page(session):
            return False
        next__page_btn = session.find_elements_by_xpath(self.next_page_button_x_path)[0]
        next__page_btn.click()
        sleep(0.4)
        return True

    def __extract_page(self, session):
        table = session.find_elements_by_xpath(self.table_x_path)[0]
        table_content = table.text
        table_content = table_content.replace('#', '')
        users = table_content.split('\n')
        users = [tuple(entry.split(' ')) for entry in users]
        return users

    def __extract_all_current_user(self, session):
        users = self.__extract_page(session)
        while self.__next_page(session):
            users += self.__extract_page(session)
        return users


def fetch_to_db():
    scatter_scraper = ScatterScraper(config.get_leaderboard_url(),
                                     config.get_table_body_x(),
                                     config.get_next_page_btn_x(),
                                     config.get_total_display_count_x(),
                                     config.get_chromedriver_path())
    users = [User.User(name=name, rank=int(rank), scatter=int(scatter)) for rank, name, scatter in
             scatter_scraper.get_all_current_user()]
    # Check for changes
    histories = []
    changed_users = []
    for user in users:
        old_user = User.get_user_by_name(user.name)
        if old_user:
            if user.scatter > old_user.scatter:
                histories.append(History.History(name=user.name, timestamp=int(time.time()), scatter=user.scatter))
                changed_users.append(user)
        else:
            changed_users.append(user)
    # Write diff to db
    User.update_all(changed_users, insert=True)
    History.insert_histories(histories)
