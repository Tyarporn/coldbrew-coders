import os
import discord
import random
import asyncio

from dotenv import load_dotenv
from discord.ext import commands, tasks


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.all()
brewmeister = commands.Bot(intents=intents, command_prefix="!")

@brewmeister.event
async def on_ready():
    for guild in brewmeister.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{brewmeister.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # members = '\n - '.join([member.name for member in guild.members]) #prints guild members
    # print(f'Guild Members:\n - {members}')

@brewmeister.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord Server!'
    )


@brewmeister.command(
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	brief="Prints pong back to the channel."
)
async def ping(ctx):
	await ctx.channel.send("pong")

@brewmeister.command(
	help="Uses some crazy logic to determine who I am.",
	brief="Returns back who I am."
)
async def info(ctx):
	await ctx.channel.send("Hello, my name is Brewmeister and I was developed by Shashanka to help automate away responsibilities humans face on a daily basis.")

@brewmeister.command(
	help="Looks like you need some help.",
	brief="Prints the list of values back to the channel."
)
async def printArgs(ctx, *args):
    response = ""
    for arg in args:
	    response = response + " " + arg

    await ctx.channel.send('Welcome {response} alumni!')


@brewmeister.event
async def on_message(message):
	if message.content == "hello":
		await message.channel.send("pies are better than cakes. change my mind.")

	await brewmeister.process_commands(message)


brewmeister.run(TOKEN)