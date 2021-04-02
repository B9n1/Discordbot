from discord.ext import commands


@commands.command()
async def join(ctx):
    await ctx.author.voice.channel.connect()


def setup(bot):
    bot.add_command(join)
