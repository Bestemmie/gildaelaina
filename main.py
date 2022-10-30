import discord, os
from discord.ui import Button, Modal, View, TextInput, Select
from discord.ext import commands
from discord.utils import get
from discord import app_commands
from dotenv import load_dotenv

load_dotenv('.env')

# GLOBAL VARS

def_color = 0xD8E1FF
token = os.environ.get('token')
welcome_ch_id = int(os.environ.get('welcome_ch_id'))

# BOT INIT

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# EVENTI

@bot.event
async def on_ready():
    print("Started ....")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands ...")
    except:
        pass

@bot.event
async def on_member_join(member: discord.Member):
    welcome_img = discord.File("./assets/imgs/welcome.jpg", filename="welcome.jpg")

    embed = discord.Embed(
        color=,
        title=f"Benvenuto sul server degli Aztecas",
        description="Ti auguriamo una buona permanenza",
    )\
        .set_image(url="attachment://welcome.jpeg")

    channel = bot.get_channel(welcome_ch_id)
    await channel.send(f"<@{member.id}>")
    await channel.send(embed=embed, files=[welcome_img])

# RUN

bot.run(token)