#!/usr/bin/env python3

from discord.ext import commands, tasks
from dirtyscatter import bot
from dirtyscatter.commands.deletemessages import clear_channel
from dirtyscatter.config import config
from dirtyscatter.events import dispatch
from dirtyscatter.events.eventType import EventType
from dirtyscatter.graphs import leaderboard, top
from dirtyscatter import db
@bot.event
async def on_ready():
    await dispatch.trigger(EventType.READY)

top.generate_plot()
bot.run(config.get_token())



