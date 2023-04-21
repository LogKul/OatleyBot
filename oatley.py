import discord
import os
import helpers

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(helpers.random_insult())

    if message.content.startswith('*'):
        await message.channel.send('It\'s so over')


client.run(os.getenv('DISCORD_BOT_TOKEN'))
