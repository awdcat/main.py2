import discord
from discord.ext import commands
import os  # ДОБАВЛИМ

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} подключён!')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Читаем токен из переменной окружения
bot.run(os.getenv("DISCORD_TOKEN"))
