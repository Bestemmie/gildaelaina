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
guild_id = int(os.environ.get('guild_id'))
welcome_ch_id = int(os.environ.get('welcome_ch_id'))
ver_ch_id = int(os.environ.get('ver_ch_id'))
ver_role_id = int(os.environ.get('ver_role_id'))

# BOT INIT

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# CLASSI

class VerifyButton(View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.timeout = None

    @discord.ui.button(label="Verificati", style=discord.ButtonStyle.green, custom_id="verificati_btn")
    async def custom_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = bot.get_guild(guild_id).get_member(interaction.user.id)
        role = bot.get_guild(guild_id).get_role(ver_role_id)
        await member.add_roles(role)
        await interaction.response.defer()

# GENERATORI

@bot.tree.command(name="verificati", description="stampa il prompt della verifica nel canale apposito")
async def print_verificati(interaction: discord.Interaction):
    verified_banner = discord.File("./assets/imgs/verificati.jpg", filename="verificati.jpg")

    embed = discord.Embed(
        color=def_color,
        title="VERIFICATI",
        description="premi il tasto per verificarti:",
    ) \
        .add_field(name="\u200b", value="\u200b")\
        .add_field(name="Sei pronto ad accedere al male?", value="proprio proprio pronto?????", inline=False)\
        .add_field(name="\u200b", value="\u200b") \
        .set_footer(text="La Gilda Elaina | 2022 - 2023")

    channel = bot.get_channel(ver_ch_id)
    await channel.send(file=verified_banner)
    await channel.send(embed=embed)
    await channel.send(view=VerifyButton())
    await interaction.response.send_message("Regole scritte con successo")

# COMANDI STAFF

@bot.tree.command(name="clear", description="pulisci il canale da n messaggi")
@app_commands.describe(n_msg = "Numero di messaggi che vuoi eliminare")
async def staff_clear(interaction: discord.Interaction, n_msg: int = 10000):
    channel = interaction.channel
    await channel.purge(limit=n_msg)
    try:
        await interaction.response.defer()
    except:
        pass

# EVENTI

@bot.event
async def on_ready():
    print("Started ....")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands ...")
    except:
        pass

    bot.add_view(VerifyButton())

@bot.event
async def on_member_join(member: discord.Member):
    welcome_img = discord.File("./assets/imgs/welcome.jpg", filename="welcome.jpg")

    embed = discord.Embed(
        color=def_color,
        title=f"Benvenuto sulla gilda di Elaina",
        description="\"Se ti chiami FEDERICOSCHI, per favore accettami l'apply\" - Depressoh",
    )\
        .set_image(url="attachment://welcome.jpg")

    channel = bot.get_channel(welcome_ch_id)
    await channel.send(f"<@{member.id}>")
    await channel.send(embed=embed, files=[welcome_img])

# RUN

bot.run(token)