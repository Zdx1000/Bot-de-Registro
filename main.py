#incorporações | Bibliotecas

import discord
from discord_components import ComponentsBot, Button, ButtonStyle

#Definindo Prefixo | Removendo comando help

bot = CoponentsBot(command_prefix="!")
bot.remove_command("help")

#Evento Bot on

@bot.event
async def on_ready():
  await bot.change_presence(
    activity=discord.Activity(type=disccord.ActivityType.streaming,
                             nome="Prefixo [ . ] | SpuBot",
                             url=str("https://www.twitch.tv/alanzoka"))) #Transmitindo a live do alanzoka
    print(f"Olá eu sou {bot.user.name} id:{bot.user.id}, Estou on")

#Comando de registro
    
@bot.command()
async def registrar(ctx):
  embed = discord.Embed(title="__**Faça seu registro abaixo**__", description="<:x_pontinho_preto:982667989763629116> Para iniciar seu registro digite o comando ``registrar``\n"
  "no chat <#iD do canal>\n"
  "<:x_pontinho_preto:982667989763629116> Caso tenha alguma __**duvida**__ basta chamar\n"
  "Suporte no chat <#Id do canal>", color=0x030303)
