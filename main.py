import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')[1:-1]
GUILD = os.getenv('DISCORD_GUILD')
intent = discord.Intents.all()
client = discord.Client(intents = intent)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
            print(f"{client.user} is connected to the following guild:\n"f"{guild.name}(id: {guild.id})")
            members = '\n - '.join([member.name for member in guild.members])
            print(f"The following users are in {guild.name}:\n - {members}")






client.run(TOKEN)
