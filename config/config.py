import getopt
import sys
import toml


try:
    opts, args = getopt.getopt(sys.argv[1:], 'c:')
    if (len(opts) == 0):
        raise Exception()
    for opt, arg in opts:
        if opt == '-c':
            config_path = arg
        else:
            raise Exception()
except:
    config_path = 'config.toml'
config = toml.load(config_path)


def get_leaderboard_url():
    global config
    url = config.get('scraper').get('leaderboard_url')
    return url


def get_table_body_x():
    global config
    table_body_x = config.get('scraper').get('table_body_x')
    return table_body_x


def get_next_page_btn_x():
    global config
    table_body_x = config.get('scraper').get('next_page_btn_x')
    return table_body_x


def get_total_display_count_x():
    global config
    table_body_x = config.get('scraper').get('total_display_count_x')
    return table_body_x


def get_fetch_interval():
    global config
    fetch_interval = config.get('general').get('fetch_interval')
    return fetch_interval
