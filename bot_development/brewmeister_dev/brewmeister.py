import endpoints as ep
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


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


@brewmeister.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord Server!'
    )


@brewmeister.command(
    help="Pass the user to ping the user",
    brief="Pings the user id passed"
)
async def ping(ctx, user_id):
    await ctx.send("<@" + user_id + ">")


@brewmeister.command(
    help="Uses some crazy logic to determine who I am.",
    brief="Returns back who I am."
)
async def info(ctx):
    string = """
    Hello, my name is Brewmeister and I was developed by
    Shashanka to help automate away responsibilities
    humans face on a daily basis.
    """

    await ctx.channel.send(string)


@brewmeister.command(
    help='!crypto BTC ---> returns BTC information',
    brief='Returns the most recent price of the passed crypto ticker'
)
async def crypto(ctx, arg):
    SYMBOL = arg
    price = round(ep.getCryptoPrice(SYMBOL), 2)

    await ctx.channel.send(f'This is the current price of {SYMBOL}: ${price}')


@brewmeister.command(
    help='tilted',
    brief='tilted'
)
async def tilted(ctx):
    await ctx.channel.send("Shashanka is tilted right now, do not disturb. :(")


@brewmeister.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send("pies are better than cakes.")

    await brewmeister.process_commands(message)


brewmeister.run(TOKEN)
