import os
import logging
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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

# Load cogs
initial_extensions = ['cogs.example_cog', 'cogs.initiate_combat']

async def main():
    async with bot:
        for extension in initial_extensions:
            await bot.load_extension(extension)
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())
