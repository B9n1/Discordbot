# bot.py
import asyncio
import discord
from discord.ext import commands
from functions import getKey
import os
from colorama import Fore, Back, Style

TOKEN = getKey('Discord')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(Back.GREEN + Fore.BLACK + f'{bot.user} has connected to Discord!')
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('write !help for help'), status=discord.Status.online)
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game('Beni´s Bester Bot V 2.0'), status=discord.Status.online)
        await asyncio.sleep(3)


for root, directories, files in os.walk('./cogs'):
    for filename in files:
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(Fore.GREEN + f'Succeeded loading: cogs.{filename[:-3]}')

        except:
            print(Fore.RED + f'Failed to load: cogs.{filename[:-3]}')


bot.run(TOKEN)
