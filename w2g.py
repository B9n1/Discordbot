import json
import requests
from discord.ext import commands


@commands.command(name='w2g', help='Creats a W2G Room.')
async def w2g(ctx):
    # Read Jason
    with open('ApiKeys.json', 'r') as myfile:
        datafile = myfile.read()
    Keys = json.loads(datafile)
    Key = str(Keys['w2g'])
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
    bot.add_command(w2g)
