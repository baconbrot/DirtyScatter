#!/usr/bin/env python3

import logging
from discord.ext import commands, tasks
from dirtyscatter import bot
from dirtyscatter.commands.deletemessages import clear_channel
from dirtyscatter.config import config
from dirtyscatter.events import dispatch
from dirtyscatter.events.eventType import EventType
from dirtyscatter.graphs import leaderboard, top
from dirtyscatter import db


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

@bot.event
async def on_ready():
    await dispatch.trigger(EventType.READY)

bot.run(config.get_token())



