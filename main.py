#!/usr/bin/env python3
import config.config
from time import sleep
from scraper import ScatterScraper

while True:
    ScatterScraper.fetch_to_db()
    print('Sleeping...')
    sleep(config.config.get_fetch_interval())
