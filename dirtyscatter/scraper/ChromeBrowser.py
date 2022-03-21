import logging

from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from time import sleep
from pyvirtualdisplay import Display
from dirtyscatter.config import config

log = logging.getLogger(__name__)

if config.get_use_virtual_display():
    display = Display(visible=False, size=(600, 400))
    log.info(f'Virtual display created')


class ChromeBrowser:

    def __init__(self, driver_location=None, headless=False):
        self.driver_location = driver_location
        self.headless = headless
        self.driver = None

    def __enter__(self):
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument('--headless')
        if self.driver_location:
            self.driver = webdriver.Chrome(self.driver_location, options=chrome_options)
        else:
            self.driver = webdriver.Chrome(options=chrome_options)
        log.debug(f'chromedriver opened')
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.close()
            log.debug(f'chromedriver closed')
