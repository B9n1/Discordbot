import json
import requests
from functions import getKey
from discord.ext import commands
from dbconnect import db_connect


class movie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # When called it Search the given query and return all the search result
    @commands.command()
    async def m_search(self, ctx, search_query):
        key = getKey('imdb')
        url = "https://imdb-api.com/en/API/Search" + key \
              + search_query
        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        jquery = json.loads(response.json())
        await ctx.print('')

    @commands.command()
    async def m_list(self, ctx):
        conn = db_connect()
        if conn:
            print("Connection Successful :)")
        else:
            print("Connection Failed :(")
        cursor = conn.cursor()
        sql_query = ("SELECT * FROM movielist")
        cursor.execute(sql_query)
        conn.close()
        await ctx


def setup(bot):
    bot.add_cog(movie(bot))
