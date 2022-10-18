import os
import discord
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # members = '\n - '.join([member.name for member in guild.members]) #prints guild members
    # print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord Server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return


    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    send_message = """
    Hello, my name is Brewmeister and I was developed by Shashanka to help automate away responsibilities humans face on a daily basis.
    """

    stonny_message = """
    Gender: Male
    Ethnicity: Chinese
    Height: Taller Than Me
    Weight: Skinny Muscular
    Hates: Most Things
    Likes: Playing Ekko
    """

    stock_ticker = """
    APPL : $150.09
    """

    if message.content == 'info!':
        response = send_message
        await message.channel.send(response)

    if message.content == 'Stoneson Liu!':
        response = stonny_message
        await message.channel.send(response)

    if message.content == 'APPL!':
        response = stock_ticker
        await message.channel.send(response)

    # @client.event
    # async def on_error(event, *args, **kwargs):
    #     with open('err.log', 'a') as f:
    #         if event == 'on_message':
    #             f.write(f'Unhandled message: {args[0]}\n')
    #         else:
    #             raise
        
# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise

client.run(TOKEN)