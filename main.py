#!/usr/bin/env python3
from discord.ext import commands
from time import sleep
from config import config
from scraper import ScatterScraper
from threading import Thread


bot = commands.Bot(command_prefix=config.get_command_prefix())


def scrape():
    while True:
        ScatterScraper.fetch_to_db()
        sleep(config.get_fetch_interval())


thread = Thread(target=scrape)
thread.start()
bot.run(config.get_token())

