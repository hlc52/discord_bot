import discord
import random
from discord import Member
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

prefix = "$"
bot = commands.Bot(command_prefix=prefix)

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

@bot.command(name='server')
async def fetchServerInfo(context):
    guild = context.guild
    await context.send(f'Server name:{guild.name}')
    await context.send(f'Server size:{len(guild.members)}')
    await context.send(f'Server name:{author.id}')

@bot.command()
async def ping(ctx):
    '''
    this text will be shown in the help command
    '''
    #get latency
    latency = bot.latency
    # send it to the user
    await ctx.send(latency)

@bot.command()
async def foo(ctx, arg):
    '''
    this is the help message for foo
    '''
    await ctx.send(arg)

@bot.command()
async def getid(ctx, member: Member):
    await ctx.send(f"Your id is {ctx.author.id}")
    await ctx.send(f"{member.mention}'s id is {member.id}")

@bot.command(name='quotey', help='spits out random quotes')
async def quotes(ctx):
    some_quotes_list = ['1','2','3'
            ]
    response = random.choice(some_quotes_list)
    await ctx.send(response)

bot.run(os.getenv('TOKEN'),bot=False)
