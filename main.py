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
  embed.set_author(name="Registre-se | BotSpy",
                   icon_url="https://cdn.discordapp.com/attachments/945064310734987264/991243063370449027/images.png")
  embed.set_image(url"https://c.tenor.com/YjrxkgoxQQwAAAAM/discord.gif")
  embed.set_thumbnall(url"https://www.gifcen.com/wp-content/uploads/2021/06/discord-gif.gif")
  embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/945064310734987264/991243063370449027/images.png",
                  text="Faça seu registro e receba seus cargos!")
  
  await ctx.send(embed=embed,
                components=[Button(label="Registra-se",
                                   custom_id="button1",
                                   emoji=bot.get_emoji(992682236463812628),
                                   disabled=False,
                                   style=2)])
  
  interacao = await bot.wait_for("button_click",
                                 check=lambda i: i.custom_id == "button1")
  
  registro = discord.Embed(title="Qual é seu gênero ?",
                           description="Cargos: \n"
                                       "<@ids dos cargos>",
                           color=0x030303)
  await interacao.send(embed=registro,
                       components=[[Button(label="Masculino", custom_id="M", emnoji"♂️", style=2),
                                    Button(label="Feminino", custom_id="F", emoji"♀️", style=2),
                                    Button(label="Não-Binário", custom_id"BI", emoji=bot.get_emoji(992679376825106512)),
                                    ]])
