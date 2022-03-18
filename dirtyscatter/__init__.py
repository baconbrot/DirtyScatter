from discord.ext import commands

from dirtyscatter.config import config

bot = commands.Bot(command_prefix=config.get_command_prefix())