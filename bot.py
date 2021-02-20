import discord
import requests
import os
import time
import random
import json
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
     time.sleep(random.randint(1,3))
     await message.channel.send(str(random.randint(0,1000000))+'%^Hello!'+str(random.randint(0,1000000)))
     
     if message.author == client.user:
         return

     if message.content.startswith('$hello'):
         time.sleep(random.randint(1,3))
         await message.channel.send('%^Hello!'+str(random.randint(0,1000000)))

     if message.content.startswith('$inspire'):
         quote = get_quote()
         await message.channel.send(quote)

client.run(os.getenv('TOKEN'), bot=False)
