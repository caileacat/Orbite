import os
import logging
import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self):
        await self.tree.sync()

bot = MyBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.tree.command(name="stop", description="Sends Orbite to the astral plane (bye bye goodnight)")
async def stop(interaction: discord.Interaction):
    await interaction.response.send_message("Orbite's colors fade, then its outline. Everything fades away until all that's left are stars ☆’ﾟ･♪:*:･｡,★’ﾟ･:*:･｡")
    await bot.close()

def send_webhook_message(webhook_url, content):
    data = {
        "content": content,
        "username": "Orbite"
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        raise Exception(f"Failed to send webhook message: {response.status_code} - {response.text}")

class InitiateCombat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="begin_combat", description="Starts combat.")
    async def begin_combat(self, interaction: discord.Interaction):
        send_webhook_message(WEBHOOK_URL, "!i begin")
        await interaction.response.send_message("Combat started using webhook.")

async def setup(bot):
    await bot.add_cog(InitiateCombat(bot))

# Load cogs
initial_extensions = ['cogs.example_cog', 'cogs.initiate_combat']

async def main():
    async with bot:
        for extension in initial_extensions:
            await bot.load_extension(extension)
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())
