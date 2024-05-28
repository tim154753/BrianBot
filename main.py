import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import pyyoutube

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')[1:-1]
GUILD = os.getenv('DISCORD_GUILD')
intent = discord.Intents.all()
#client = discord.Client(intents = intent)
bot = commands.Bot(command_prefix='!', intents=intent)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
            print(f"{bot.user} is connected to the following guild:\n"f"{guild.name}(id: {guild.id})")
            members = '\n - '.join([member.name for member in guild.members])
            print(f"The following users are in {guild.name}:\n - {members}")
@bot.command(name='hello')
async def insult(ctx):
    '''if message.author == bot.user:
        return'''
    #if message.content == "/hello":
    sep = '#'
    victim = str(ctx.author).split(sep,1)[0]
    await ctx.channel.send(f"Hello {victim}! Why are you gay?")

@bot.command(name='play')
async def joinCall(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(name='leave')
async def leave(ctx):
    if ctx.voice_client is not None:
        print("Test 1")
        await ctx.voice_client.disconnect(force=True)
        print("Test 2")
    else:
        await ctx.send("I'm not in a voice call idiot")









bot.run(TOKEN)
