import endpoints as ep
import discord
import os
form dotenv import load_dontenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
crisco = commands.Bot(intents=intents, command_prefix = "!")

@crisco.event
async def on_ready():
    for guild in crisco.guilds:
        if guild.name == GUILD:
            break
