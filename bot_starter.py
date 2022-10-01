import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTAyNTg1MjYwNTI1NzIyMDEwNg.GPwgX9.2H15jMg3LgbnMq3oQso9MTeop1a3XFZJNp1s2E')
