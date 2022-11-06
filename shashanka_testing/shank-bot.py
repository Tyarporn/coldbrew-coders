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
)
async def ping(ctx):
    await ctx.channel.send("pong!")

@brewmeister.command()
async def info(ctx):
	await ctx.channel.send("Hello, my name is Brewmeister and I was developed by Shashanka to help automate away responsibilities humans face on a daily basis.")

# prints out arguments that were passed to it
@brewmeister.command()
async def printArgs(ctx, *args):
    response = ""
    
    for arg in args:
	    response = response + " " + arg

    await ctx.channel.send('Welcome {response} alumni!')


# @brewmeister.event
# async def on_message(message):
#     if message.author == brewmeister.user:
#         return


#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]
#     send_message = """
#     Hello, my name is Brewmeister and I was developed by Shashanka to help automate away responsibilities humans face on a daily basis.
#     """

#     stonny_message = """
#     Gender: Male
#     Ethnicity: Chinese
#     Height: Taller Than Me
#     Weight: Skinny Muscular
#     Hates: Most Things
#     Likes: Playing Ekko
#     """

#     stock_ticker = """
#     APPL : $150.09
#     """

#     sis_message = """
#     Hello Sharbani, this is Shashanka's bot greeting you!
#     """

#     if message.content == 'info!':
#         response = send_message
#         await message.channel.send(response)

#     if message.content == 'Stoneson Liu!':
#         response = stonny_message
#         await message.channel.send(response)

#     if message.content == 'APPL!':
#         response = stock_ticker
#         await message.channel.send(response)
    
#     if message.content == 'Sharbani!':
#         response = sis_message
#         await message.channel.send(response)

brewmeister.run(TOKEN)