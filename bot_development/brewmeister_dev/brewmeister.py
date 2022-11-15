from header_files import *
import endpoints as ep

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
	help="Pass the user id into the command and it will ping that user in the server",
	brief="Pings the user id passed"
)
async def ping(ctx, user_id):
    await ctx.send("<@" + user_id + ">")

@brewmeister.command(
	help="Uses some crazy logic to determine who I am.",
	brief="Returns back who I am."
)
async def info(ctx):
	await ctx.channel.send("Hello, my name is Brewmeister and I was developed by Shashanka to help automate away responsibilities humans face on a daily basis.")

@brewmeister.command(
    help='!crypto BTC ---> returns BTC information',
    brief='Returns the most recent price of the passed crypto ticker'
)
async def crypto(ctx, arg):
    SYMBOL = arg
    price = round(ep.getCryptoPrice(SYMBOL),2)

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
		await message.channel.send("pies are better than cakes. change my mind.")

	await brewmeister.process_commands(message)


brewmeister.run(TOKEN)