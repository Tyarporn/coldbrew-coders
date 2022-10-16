import os

import discord 
from dotenv
import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
client.run(TOKEN)