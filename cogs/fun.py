from discord.ext import commands
import random
import time


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='decider', help='Decide for you one of the options.')
    async def decider(self,ctx, *, txt="Yes or No"):
        txt = txt.replace(" oder ", " or ")
        options = txt.split(" or ")
        response = random.choice(options)
        await ctx.send(f'I choose you: {response}')

    @commands.command(name='repeat', help='Repeats a message')  # Bot repeats the message n times
    async def repeat(self,ctx, times: int, content='repeating...'):
        """Repeats a message multiple times."""
        for i in range(times):
            await ctx.send(content)

    @commands.command(name='selfdestruction', help='Initiate Self Destruction')
    async def selfdestruction(self,ctx):
        await ctx.send(f'!!SELF DESTRUCTION INITIATED!!')
        await ctx.send(f'COUNT DOWN:')
        for i in range(10):
            time.sleep(1)
            await ctx.send(10 - i)
        await ctx.send('<:youtried:596576824872402974>')

    @commands.command(name='massawalk', help='Makes a Massawalk kekw.')
    async def votekick(self,ctx):
        await ctx.send(f':MassaWalk: :MassaWalk: :MassaWalk: :MassaWalk: :MassaWalk:')

    @commands.command(name='wah', help='Wuerfelt auf Humor')
    async def wah(self, ctx, erschwaert=0):
        humor = 50+erschwaert
        wurfel= random.randint(0, 100)
        goodResponse = ["HAHA, Der war gut. XD", "Nice, der war mega!!", "Legendär!", "Man habe ich mich weggeschmissen!", "Das war ein Hammer!"]
        badResponse = ["Och nö der Musste wirklich nicht sein", "Der war Schmutz!", "Geh dich vergraben!", "Da ist die Tür.", "Der ist so low wie du in CS!"]
        if wurfel <= humor:
            response = goodResponse[random.randint(0, 4)]
        else:
            response = badResponse[random.randint(0, 4)]

        await ctx.send(response)


def setup(bot):
    bot.add_cog(fun(bot))
