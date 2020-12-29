# bot.py
import asyncio
import random
import os
import discord
from discord.ext import commands
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions

TOKEN = ''

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


@bot.command(name='decider', help='Decide for you one of the options.')
async def decider(ctx, *, txt="Yes or No"):
    txt = txt.replace(" oder ", " or ")
    options = txt.split(" or ")
    response = random.choice(options)
    await ctx.send(f'I choose you: {response}')


@bot.command(name='repeat', help='Repeats a message')  # Bot repeats the message n times
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command(name='selfdestruction', help='Initiate Self Destruction')
async def selfdestruction(ctx):
    await ctx.send(f'!!SELF DESTRUCTION INITIATED!!')
    await ctx.send(f'COUNT DOWN:')
    for i in range(10):
        time.sleep(1)
        await ctx.send(10-i)
    await ctx.send('<:youtried:596576824872402974>')


@bot.command(name='w2g')
async def w2g(ctx):
    options = FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(executable_path='/home/ubuntu/github/Discordbot/geckodriver',options=options)
    driver.get("http://www.w2g.tv")

    # click coockie button
    #driver.find_element_by_xpath("//button[@class='sc-ifAKCX dvvOSu']").click()
    #time.sleep(1)
    # Create Room
    driver.find_element_by_xpath("//button[@class='ui big primary button loading_button']").click()
    # Joins Room
    driver.find_element_by_xpath("//div[@class='ui fluid green cancel button']").click()
    # Copy Room Inv
    driver.find_element_by_xpath("//div[@class='invite-cta w2g-search-hide w2g-users']").click()
    link = driver.find_element_by_xpath("//input[@class='invite-url']").get_attribute("value")
    driver.close()
    await ctx.send(link)


@bot.command(name='vote kick', help='Decide for a vote kick.')
async def votekick(ctx, name: str):
    await ctx.send(f'Yes')


bot.run(TOKEN)
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
