import os
import discord
import random
import asyncio

from dotenv import load_dotenv
from discord.ext import commands, tasks
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


intents = discord.Intents.all()
brewmeister = commands.Bot(intents=intents, command_prefix="!")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
COIN_API = os.getenv('COINMARKETCAP_API_KEY')
COIN_URL = os.getenv('CMC_URL')