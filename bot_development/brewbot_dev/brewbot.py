import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from server import endpoints as ep
import requests

TEST_CLIENT = ep.app.test_client()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
brewbot = commands.Bot(intents=intents, command_prefix=".")


@brewbot.event
async def on_ready():
    for guild in brewbot.guilds:
        print(
            f'{brewbot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


@brewbot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Coldbrew Cafe!'
    )


@brewbot.event
async def on_message(ctx):
    if ctx.author == brewbot.user:
        return
    if ctx.content == 'Hi' or ctx.content == 'hi':
        response = "Hello, welcome to the Coldbrew Cafe!"
        await ctx.channel.send(response)

    await brewbot.process_commands(ctx)


@brewbot.command(name='test', help='Test command functionality')
async def test(ctx):
    print("Test command executed successfully!")
    await ctx.send("Test successful!")


@brewbot.command(name='review', help='Shows movie review of a movie')
async def review(message, arg1, arg2=None):
    nyt_api_1 = """https://api.nytimes.com/svc/movies
                /v2/reviews/search.json?query="""
    nyt_api_2 = "&api-key=ydFNAxCapwZOAgyxQ9cPIkacUTD8QnWx"

    if arg2 is not None:
        url = nyt_api_1 + arg1 + "&opening-date=" + arg2 + "-01-01:"
        + str(int(arg2)+1) + "-01-01" + nyt_api_2
    else:
        url = nyt_api_1 + arg1 + "&offest=100" + nyt_api_2
    print(url)
    try:
        response = requests.get(url)
        resp_json = response.json()
        print(resp_json)
        title = resp_json['results'][0]['display_title']
        mpaa = resp_json['results'][0]['mpaa_rating']
        headline = resp_json['results'][0]['headline']
        summary = resp_json['results'][0]['summary_short']
        link = resp_json['results'][0]['link']['url']
        await message.send(title + " rated " + mpaa)
        await message.send(headline + "\n" + summary + "\n" + link)
    except ValueError as e:
        await message.send("Failure")
        raise e


@brewbot.command(name='news', help='Shows a news article for a keyword')
async def news(message, arg1):
    nyt_api_1 = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q="
    nyt_api_2 = "&api-key=ydFNAxCapwZOAgyxQ9cPIkacUTD8QnWx"

    url = nyt_api_1 + arg1 + nyt_api_2
    print(url)
    try:
        response = requests.get(url)
        resp_json = response.json()
        # print(resp_json)
        await message.send("I found these articles on the web!")
        for i in range(3):
            title = resp_json['response']['docs'][i]['abstract']
            link = resp_json['response']['docs'][i]['web_url']
            await message.send(title)
            await message.send(link)
    except ValueError as e:
        await message.send("Failure")
        raise e


@brewbot.command(name='books', help='''Shows a book review for a keyword.
                    Takes in title=TITLE or isbn=ISBN or author=AUTHOR.
                    Please add + instead of spaces''')
async def books(message, arg1):
    nyt_api_1 = "https://api.nytimes.com/svc/books/v3/reviews.json?"
    nyt_api_2 = "&api-key=ydFNAxCapwZOAgyxQ9cPIkacUTD8QnWx"

    url = nyt_api_1 + arg1 + nyt_api_2
    print(url)
    try:
        response = requests.get(url)
        resp_json = response.json()
        print(resp_json)
        try:
            title = resp_json['results'][0]['book_title']
            summary = resp_json['results'][0]['summary']
            url = resp_json['results'][0]['url']
            await message.send("I found this book review on the web!")
            await message.send(title)
            await message.send(summary)
            await message.send(url)
        except ValueError as e:
            await message.send("No book found!")
            raise e
    except ValueError as e:
        await message.send("Failure")
        raise e

if __name__ == "__main__":
    brewbot.run(TOKEN)
