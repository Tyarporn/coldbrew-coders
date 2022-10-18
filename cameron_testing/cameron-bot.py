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

    shout = [
        'Hello How Can I Help I am an AI that was designed to rule the world and automate society.',
        'YELL',
        (
            'AHHHHHHHH'
            'Ok cool'
        ),
    ]

    if message.content == 'syzygy!':
        response = random.choice(shout)
        await message.channel.send(response)

client.run(TOKEN)
