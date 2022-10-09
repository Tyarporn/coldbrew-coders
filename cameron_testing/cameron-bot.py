# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


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
        'SCREAM',
        'YELL',
        (
            'AHHHHHHHH'
            'Ok cool'
        ),
    ]

    if message.content == '!syzygy':
        response = random.choice(shout)
        await message.channel.send(response)

client.run(TOKEN)
