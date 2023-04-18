# import endpoints as ep
import discord
import os
import asyncio
import requests
# from dotenv import load_dontenv
from discord.ext import commands

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

intents = discord.Intents.all()
crisco = commands.Bot(intents=intents, command_prefix="!")

@crisco.event
async def on_ready():
    for guild in crisco.guilds:
        if guild.name == GUILD:
            break

async def on_ready():
    print("User {0.user}".format(client))

async def send_live_crisco():
    while True:
        response = requests.get('https://cricapi.com/api/matches?apikey=your_api_key')
        data = response.json()
        #gets cricket score from API

        message = ''
        for match in data['matches']:
            message += f"{match['team-1']} vs {match['team-2']}: {match['score']}\n"
        #parses the data and puts it in message form

        channel = client.get_channel(your_channel_id)
        await channel.send(message)
        #message is sent to discord server

        await asyncio.sleep(60)
        #update every minute for next live score

client.run('your_bot_token')
