import discord
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
    await bot.change_presence(activity = discord.Game(name = 'Your mom'))
    for guild in bot.guilds:
        print(guild)
            
    print(
            f'-----------------------'
            f'{bot.user} is connected to the follwing guild:\n'
            f'{guild.name}(id: {guild.id})\n'
            )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

'''
@bot.event
async def on_message(message):
    print("The msgs content was:", message.content)
'''
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

bot.run(os.getenv('TOKEN'),bot=False)
