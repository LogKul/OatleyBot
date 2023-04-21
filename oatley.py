# bot.py
import os
import random
import requests
import json

import discord
from dotenv import load_dotenv

import helpers

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.add_reaction(reaction.emoji)


@client.event
async def on_reaction_remove(reaction, user):
    flag = False
    async for user in reaction.users():
        if user == client.user:
            flag = True

    if (reaction.count == 1 & flag == True):
        await reaction.remove(client.user)


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return

    await message.channel.send('I saw what you deleted, ' + helpers.desc_noun())


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    insult = helpers.random_insult()

    if message.content.startswith('&oatley'):
        await message.channel.send(insult)

    elif message.content.startswith('&csLEgo'):
        await message.channel.send(file=discord.File('./media/dvcsgo.mp4'))

    elif message.content.startswith('&save'):
        if message.attachments[0]:
            a = message.attachments[0]

            # Write to file
            media = requests.get(a.url, allow_redirects=True)
            open('./media/' + a.filename, 'wb').write(media.content)

            # Parse user's command name
            command = message.content.split()[1]

            # Create DB link
            f = open('db.json')
            db = json.load(f)
            f.close()
            db["saved_media"][command] = './media/' + a.filename
            updated_db = json.dumps(db, indent=4)
            with open("db.json", "w") as outfile:
                outfile.write(updated_db)

            await message.channel.send('File saved, ' + helpers.desc_noun())

    elif message.content.startswith('&getall'):
        f = open('db.json')
        db = json.load(f)
        f.close()

        # Text processing
        output_str = "All saved media:\n```"
        for key in db["saved_media"]:
            output_str += (key + ', ')
        output_str = output_str[:-2]
        output_str += '```'

        await message.channel.send(output_str)

    elif message.content.startswith('&get'):
        command = message.content.split()[1]

        f = open('db.json')
        db = json.load(f)
        f.close()

        await message.channel.send(file=discord.File(db["saved_media"][command]))

    else:
        num = random.random()
        if num > 0.99:
            await message.channel.send('Mom would be sad')
        elif num > 0.96:
            await message.channel.send('It\'s so fucking over')
        elif num > 0.9:
            await message.channel.send('It\'s so over')

    # if message.content.startswith('&oatley'):
    #    await message.channel.send('It\'s so over')

client.run(TOKEN)
