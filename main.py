from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

@app.route('/')
def home():
    return "Бот работает!"

def run_web():
    app.run(host='0.0.0.0', port=3000)

Запуск Flask-сервера в отдельном потоке
Thread(target=run_web).start()

=== Настройка Discord-бота ===
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Бот {bot.user} подключён и активен!')

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

token = os.getenv("DISCORD_TOKEN")

if token:
    bot.run(token)
else:
    print("❌ Токен не найден. Убедись, что DISCORD_TOKEN задан в Render.")
