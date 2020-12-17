# bot.py
import asyncio
import random
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
################################################################################################
#                                          Bot Events                                          #
################################################################################################

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    bot.loop.create_task(status_task())


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
       f'{member.name} has joined the party!!!!')


async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('write !help for help'), status=discord.Status.online)
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game('Beni´s Bester Bot V 1.0'), status=discord.Status.online)
        await asyncio.sleep(3)
################################################################################################
#                                          Bot Commands                                        #
################################################################################################


@bot.command(name='decide', help='Decide for you one of the options.')
async def decider(ctx, *, txt="Yes or No"):
    txt = txt.replace(" oder ", " or ")
    options = txt.split(" or ")
    response = random.choice(options)
    await ctx.send(f'I choose you: {response}')


bot.run('NzU1OTAxOTE2MDcxOTg1MTcz.X2KChA.RMjdYLQdVL1C5A-5K4897TMa_Rw')
################################################################################################
#                                       Code Graveyard                                         #
################################################################################################
"""
@client.event
async def on_message(message):
    if message.author.bot:
        return
    await message.channel.send('Du hast geschickt : {}'.format(message.content))
"""