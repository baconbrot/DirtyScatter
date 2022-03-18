from dirtyscatter import bot
from dirtyscatter.config import config


async def clear_channel(channel):
    msgs = []
    text_channel = bot.get_channel(channel)
    async for x in text_channel.history(limit=100):
        msgs.append(x)
    await text_channel.delete_messages(msgs)
