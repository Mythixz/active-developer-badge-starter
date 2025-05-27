from dotenv import load_dotenv, find_dotenv
import os
import discord
from discord.ext import commands

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')
print(f"TOKEN: {TOKEN}")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="ping", description="Check if bot is online!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓กำลัง Active")

bot.run(TOKEN)
