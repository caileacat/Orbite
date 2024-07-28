import discord
from discord.ext import commands
from discord import app_commands

class InitiateCombat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="begin_combat", description="Starts combat.")
    async def begin_combat(self, interaction: discord.Interaction):
        await interaction.response.send_message("Combat started.")

async def setup(bot):
    await bot.add_cog(InitiateCombat(bot))
