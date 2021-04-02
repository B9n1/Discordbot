import json
import requests
from mysql.connector import connect, Error
from discord.ext import commands
from dbconnect import db_connect


@commands.command()
async def m_search(ctx, search_query):
    # Read Jason
    with open('ApiKeys.json', 'r') as myfile:
        datafile = myfile.read()
    Keys = json.loads(datafile)
    Key = str(Keys['imdb'])

    url = "https://imdb-api.com/en/API/Search" + Key \
          + search_query
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    await ctx.print(response.text.encode('utf8'))


@commands.command()
async def m_add():
    # Read Jason
    with open('ApiKeys.json', 'r') as myfile:
        datafile = myfile.read()
    Keys = json.loads(datafile)
    Key = str(Keys['imdb'])


@commands.command()
async def m_list(ctx):
    try:
        conn = db_connect()
    except Error as e:
        print(e)
    db_curso = db_connecttion.cursor()
    await ctx




def setup(bot):
    bot.add_command(m_search,m_add, m_list)