# bot.py
import asyncio
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('discord.gg/devsky'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('MeinBot!'), status=discord.Status.online)
        await asyncio.sleep(3)

async def on_massage(message):
    if message.author.user.bot:
        return
    await message.chanel.send('Du hast geschickt : {}' .format(message.content))




client.run('NzU1OTAxOTE2MDcxOTg1MTcz.X2KChA.RMjdYLQdVL1C5A-5K4897TMa_Rw')