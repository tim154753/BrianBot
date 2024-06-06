import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import yt_dlp
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')[1:-1]
intent = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intent)

voice_clients = {}
yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)

ffmpeg_options = {'before_options': "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", 'options': '-vn -filter:a "volume=0.25"'}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
            print(f"{bot.user} is connected to the following guild:\n"f"{guild.name}(id: {guild.id})")
            members = '\n - '.join([member.name for member in guild.members])
            print(f"The following users are in {guild.name}:\n - {members}")

@bot.command(name='hello')
async def insult(ctx):
    await ctx.channel.send(f"Hello {ctx.author.name}! , file=discord.File('path')) #put path of file you want to send as message here

@bot.command(name='stop')
async def leave(ctx):
    if ctx.voice_client is not None:
        try:
            voice_clients[ctx.guild.id].stop()
            await ctx.voice_client.disconnect()
        except Exception as e:
            print(e)
    else:
        await ctx.send("I'm not in a voice channel idiot")

@bot.command(name='play')
async def joinCall(ctx):
    if ctx.author.voice is None:
        await ctx.send(f"You're not in a voice channel {ctx.author.name}. No trolling for you!")
    else:
        try:
            voice_client = await ctx.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except Exception as e:
            print(e)
        try:
            url = ctx.message.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download = False))

            song = data['url']
            player = discord.FFmpegOpusAudio(song, **ffmpeg_options, executable = 'C:/ffmpeg/ffmpeg.exe') # put path of ffmpeg executable in quotes

            voice_clients[ctx.guild.id].play(player)
        except Exception as e:
            print(e)

@bot.command(name='pause')
async def pauseAudio(ctx):
    try:
        voice_clients[ctx.guild.id].pause()
    except Exception as e:
        print(e)
@bot.command(name='resume')
async def resumeAudio(ctx):
    try:
        voice_clients[ctx.guild.id].resume()
    except Exception as e:
        print(e)







bot.run(TOKEN)
