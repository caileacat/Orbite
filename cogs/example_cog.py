import discord
from discord.ext import commands
from discord import app_commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Says hello!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello, world!")

async def setup(bot):
    await bot.add_cog(ExampleCog(bot))
