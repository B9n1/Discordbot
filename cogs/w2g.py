import json
import requests
from discord.ext import commands
from functions import getKey


class w2g(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='w2g', help='Creats a W2G Room.')
    async def w2g(self, ctx):
        Key = getKey('w2g')
        w2g_data = {
            "w2g_api_key": Key,
            "share": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "bg_color": "#000000",
            "bg_opacity": "50"
        }
        request = requests.post(url="https://w2g.tv/rooms/create.json", data=w2g_data)
        response = json.loads(request.text)
        await ctx.send(f"https://w2g.tv/rooms/" + str(response["streamkey"]))


def setup(bot):
    bot.add_cog(w2g(bot))
