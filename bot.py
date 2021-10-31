from aiohttp.http import RESPONSES
import discord
from discord import colour
from discord import embeds
from discord.activity import Streaming
from discord.errors import ClientException
from discord.ext import commands
import random 
from os import name, urandom
import asyncio,youtube_dl
from dotenv import load_dotenv
from discord.ext.commands.cooldowns import BucketType
load_dotenv()
client = commands.Bot(command_prefix='.')

#client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Streaming(name='Come watch', url=f'https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    print('The bot is online now {0.user}'.format(client))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.purge(limit=1)
        await ctx.send('pooping rn {:.2f}s remaining'.format(error.retry_after))

@client.command(aliases= ['ping'])
async def poop(ctx):
 ping = client.latency * 1000
 await ctx.send(f'poop returned in {round(ping / 5)}ms')

@client.command()
async def commandlist(ctx):
 await ctx.send('.poop, .predict, .what_da_bot_doin')  

@client.command()
async def what_da_bot_doing(ctx):
 await ctx.send('Streaming come check it out')

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def predict(ctx, *, question):
 responses = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes and possible Diarrhoea.",
"Don't count on it.",
"I would say no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful.",
"You would have better chances at getting a gf/bf",
"Some trolling might happen",
"I will suck you into this black hole(totally unrelated to the question you asked)"]
 
 await ctx.send(f'{random.choice(responses)}')


@client.command()
async def say(ctx, *, arg):
 await ctx.message.delete()
 whitelist = [451991202926166021] 

 if ctx.author.id not in whitelist:
           return
 else: await ctx.send(arg)

client.run('ODE0NzAzODExNDc4MjkwNDUy.YDhuDQ.X6G1Ie8yF8foNJbCT_q_ObYZCU4'
