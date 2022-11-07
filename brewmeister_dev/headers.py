import os
import discord
import random
import asyncio

from dotenv import load_dotenv
from discord.ext import commands, tasks
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json