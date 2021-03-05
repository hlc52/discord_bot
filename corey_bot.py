import discord
import random
from discord import Member
from discord import Color
from discord.ext import commands
from dotenv import load_dotenv
import os
import json

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.presences = True #you need this bc the member cache won't update w/o it. the cache would only cache at start of bot and status won't update
prefix = "$"
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print("Everything's all ready to go")
    await bot.change_presence(activity = discord.Game(name = 'your favoruite game'))
    for guild in bot.guilds:
        print(guild)
            
    print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
            f'{bot.user.name} has connected to discord')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    guild = discord.utils.get(bot.guilds, name='Chicken')
    print(guild.name)

@bot.command(name='server', help='get server stats')
async def fetchServerInfo(context):
    guild = context.guild
    await context.send(
            f'-----\n'
            f'server name: {guild.name}\n'
            f'server channels: {len(guild.channels)}\n'
            f'server members: {guild.member_count}\n'
)
@bot.command(name='coreypic', help='get a pic for a corey lick')
async def corey_img(context):
    await context.send(file = discord.File('corey.png'))

@bot.command(name='coreyolive', help='check if corey is online')
async def coreyStatus(ctx):
    #corey_id = 139598054373195776 #my testing id
    corey_id = 225359460812455936 #coreys id
    
    corey_member = ctx.guild.get_member(corey_id)
    corey_stat = corey_member.status
    result = ""
    filename = ''

    if str(corey_stat) == "offline":
        result = "corey ded"
        filename = "corey_slep.png"
        color = Color.red()
    else:
        result = "!!!ALERT!!! COREY OLIVE"
        filename = "corey_online.png"
        color = Color.green()
    
    embedVar = discord.Embed(title="COREY STATUS", color=color)
    file = discord.File(filename)
    embedVar.add_field(name="Is Corey Hecking Alive?", value=result, inline=False)
    embedVar.add_field(name="mobile",value=corey_member.mobile_status, inline=True)
    embedVar.add_field(name="pc",value=corey_member.desktop_status, inline=True)
    embedVar.set_image(url="attachment://" + filename)
    await ctx.send(embed=embedVar, file=file)

@bot.command()
async def getid(ctx, member: Member):
    await ctx.send(f"Your id is {ctx.author.id}")
    await ctx.send(f"{member.mention}'s id is {member.id}")

@bot.command(name='8ball', help='spits out random 8 ball phrases')
async def quotes(ctx):
    some_quotes_list = ['yes','no','maybe','roll again']
    response = "8 ball says: " + random.choice(some_quotes_list)
    await ctx.send(response)

bot.run(os.getenv('COREY_TOKEN'))
