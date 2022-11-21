import os
import discord
import random
import asyncio
import json
# import pytest

from dotenv import load_dotenv
from discord.ext import commands, tasks
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


intents = discord.Intents.all()
brewmeister = commands.Bot(intents=intents, command_prefix="!")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')