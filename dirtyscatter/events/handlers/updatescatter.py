

import discord
from discord.ext import tasks

from dirtyscatter import bot
from dirtyscatter.commands.deletemessages import clear_channel
from dirtyscatter.config import config
from dirtyscatter.events.dispatch import register
from dirtyscatter.events.eventType import EventType
from dirtyscatter.graphs import leaderboard, top
from dirtyscatter.scraper.ScatterScraper import fetch_to_db


async def send_plot(file):
    with open(file, 'rb') as f:
        picture = discord.File(f)
        channel = bot.get_channel(config.get_channel_id())
        await channel.send(file=picture)


@tasks.loop(seconds=config.get_fetch_interval())
async def send_plots():
    fetch_to_db()
    lb = leaderboard.generate_plot()
    tp = top.generate_plot()
    await clear_channel(config.get_channel_id())
    await send_plot(lb)
    await send_plot(tp)


@register(EventType.READY)
async def on_ready():
    send_plots.start()
