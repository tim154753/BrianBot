import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import functions
import yt_dlp

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')[1:-1]
intent = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intent)

voice_clients = {}
yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)

ffmpeg = {"options": '-vn'}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
            print(f"{bot.user} is connected to the following guild:\n"f"{guild.name}(id: {guild.id})")
            members = '\n - '.join([member.name for member in guild.members])
            print(f"The following users are in {guild.name}:\n - {members}")

@bot.command(name='hello')
async def insult(ctx):
    await ctx.channel.send(f"Hello {ctx.author.name}! \nYou look lonely. I can fix that.", file=discord.File('C:/Users/Timmy/Pictures/Screenshots/beautiful2.png'))

@bot.command(name='play')
async def joinCall(ctx):
    if ctx.author.voice is None:
        await ctx.send(f"You're not in a voice channel {ctx.author.name}. No trolling for you!")
    else:
        channel = ctx.author.voice.channel
        await channel.connect()

@bot.command(name='leave')
async def leave(ctx):
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not in a voice channel idiot")
    
