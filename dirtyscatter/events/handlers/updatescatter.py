

import discord
from discord.ext import tasks

from dirtyscatter import bot
from dirtyscatter.commands.deletemessages import clear_channel
from dirtyscatter.config import config
from dirtyscatter.events.dispatch import register
from dirtyscatter.events.eventType import EventType
from dirtyscatter.graphs.leaderboard import generate_plot


@tasks.loop(seconds=config.get_fetch_interval())
async def send_plot():
    await clear_channel(config.get_channel_id())
    generate_plot()
    with open('output.png', 'rb') as f:
        picture = discord.File(f)
        channel = bot.get_channel(config.get_channel_id())
        await channel.send(file=picture)


@register(EventType.READY)
async def on_ready():
    send_plot.start()
