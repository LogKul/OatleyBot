import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('*'):
        await message.channel.send('It\'s so over')

client.run(os.getenv('TOKEN'))
