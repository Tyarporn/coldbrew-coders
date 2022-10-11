import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Coldbrew Cafe!'
    )

@client.event
async def on_message(message):
    print(message)
    print(message.author, client.user, message.content, message.channel)

    if message.author == client.user: # check if sender is bot itself (avoids recursion)
        return

    brew_bot_responses = [
        'Hi, how can I help you?',
        'Hey, what can I do for you today?',
        'Hello! How can I serve you?'
    ]

    if message.content == '!coffee':
        response = random.choice(brew_bot_responses)
        await message.channel.send(response)

client.run(TOKEN)
