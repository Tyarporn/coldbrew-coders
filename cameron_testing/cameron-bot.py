# bot.py
import os
import random
impot discord
import datetime
from dotenv import load_dotenv
import yfinance as yf


# https://pypi.org/project/yfinance/
#API I Plan on using with documentation for stocks


stock_tickers = ['AAPL', 'AMZN', 'MSFT', 'GOOGL']
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

    if message.content == '$help':
        response = helpResponse
        await message.channel.send(response)
    
    elif message.content.startswith("$price"):
        _ticker = message.content.split(' ')[1] #updated to work with various tickers
        #upon calling the $price command, will make yfinance api call to whatever ticker is indicated
        _ticker = yf.Ticker(_ticker)
        response = _ticker.info
    
    elif message.content == "$change":
        response = changeResponse

@client.command(name='$TEST')
async def test(ctx):
    print("Test!")
    await ctx.send("Test successful!")
    
client.run(TOKEN)
