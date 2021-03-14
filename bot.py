# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #open text file in read mode
    text_file = open("words.txt", "r")

    #read whole file to a string
    words = text_file.read()

    loopNum = random.randint(3,10)
    sentence = ""

    if message.content.lower() == 'alias' or message.content.split() == 'alias' or message.content.split() == 'Alias':
      if words is not None:
        words = words.split('\n')
        for x in range(loopNum):
          index = random.randint(0,466550)
          sentence = sentence + words[index] + " "
          print(sentence)
        response = sentence
        await message.channel.send(response)
      else:
        response = "Uh oh there's been a fucky wucky"
        await message.channel.send(response)

client.run(TOKEN)
