import discord
from discord.ext.commands import Bot, Cog

client = Bot(command_prefix='!')
@client.event
async def on_ready():
    print(f'Logged in as {client.user_name}{client user.id}')
    await client.change_presence(status=discord.Status.online)

@client.event
async def on_message(msg):
    if msg.content == "no run":
        await client.close()
    elif msg.content.startswith('hi there'):
        await msg.channel.send('yo')


 