import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} подключён!')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("MTM4MjQ2Mjk1MTAwNDMwNzUwNg.GOVp5J.AIX_3p-LW1v9t98rBPXbNIru08pZsA1PpsnOYQ")
