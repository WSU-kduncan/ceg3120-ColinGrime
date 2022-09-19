import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    suntzu_quotes = [
        'Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.',
        'In the midst of chaos, there is also opportunity.',
        'He will win who knows when to fight and when not to fight.',
    ]

    if message.content == 'suntzu!':
        response = random.choice(suntzu_quotes)
        await message.channel.send(response)
    elif message.content == 'catme!':
        await message.channel.send(file=discord.File(random.choice(('cat1.jpg', 'cat2.jpg', 'cat3.jpg'))))

client.run(TOKEN)
