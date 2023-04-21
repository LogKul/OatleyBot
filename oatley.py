# bot.py
import os
import random
import helpers

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    insult = helpers.random_insult()
    
    if message.content.startswith('&oatley'):
        await message.channel.send(insult)
    else:
        num = random.random()
        if num > 0.8:
            await message.channel.send('It\'s so over')
        elif num > 0.95:
            await message.channel.send('It\'s so fucking over')
        elif num > 0.99:
            await message.channel.send('Mom would be sad')
    
    
    #if message.content.startswith('&oatley'):
    #    await message.channel.send('It\'s so over')

client.run(os.getenv('DISCORD_BOT_TOKEN'))