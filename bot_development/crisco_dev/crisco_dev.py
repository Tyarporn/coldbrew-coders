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


# @crisco.event
# async def on_ready():
#     for guild in crisco.guilds:
#         if guild.name == GUILD:
#             break

#
#async def on_ready():
#    print("User {0.user}".format(client))
    
#@brewbot.event
#async def on_member_join(member):
#    async def on_member_join(member):
#        await member.create_dm()
#        await member.dm_channel.send(
#            "Hi {member.name}, welcome to the Coldbrew Cafe!"
        )
#@brewbot.event
#async def on_message(ctx):
#    if ctx.author == brewbot.user:
#        return
#    if ctx.content == "Hi" or ctx.content == "hi"
#    reponse = "Hello, welcome to the Coldbrew Cafe!"
#    await ctxx.channel.send(response)
    
#   await brewbot.process_commands(ctx)


async def send_live_crisco():
    crisco_url = 'https://cricapi.com/api/matches?apikey=your_api_key'
    while True:
        response = requests.get(crisco_url)
        data = response.json()
        # gets cricket score from API

        message = ''
        for match in data['matches']:
            message += f"{match['team-1']} vs {match['team-2']}: {match['score']}\n"
        # parses the data and puts it in message form

        your_channel_id = None  # PLACEHOLDER FOR FLAKE8  - Ty
        channel = client.get_channel(your_channel_id)
        await channel.send(message)
        # message is sent to discord server

        await asyncio.sleep(60)
        # update every minute for next live score

client.run('your_bot_token')
