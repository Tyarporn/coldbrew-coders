# bot.py
import os
import random
import discord
from dotenv import load_dotenv

intents = discord.Intents.all()
client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    helpResponse = "Here is a list of commands: !price $TICKER, !change $TICKER"
    priceResonse = "The current price is: "
    changeResponse = "The change of this stock over the last year is: "

    if message.content == '!help':
        response = helpResponse
        await message.channel.send(response)
    
    else if message.content == "!price":
        response = currentPrice
    
    else if message.content == "!change":
        response = changeResponse

client.run(TOKEN)
