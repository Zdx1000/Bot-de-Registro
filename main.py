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
                                    Button(label="Não-Binário", custom_id="BI", emoji=bot.get_emoji(992679376825106512)),
                                    Button(label="Avançar", custom_id="AV", emoji=bot.get_emoji(985174071559979068), style=ButtonStyle.blue, disabled=True),
                                    Button(label="Voltar", custom_id="VL", emoji=bot.get_emoji(985174071559979068), style=ButtonStyle.red, disabled=True)]])
  
  interacao2 = await bot.wait_for("button_click", check=lambda i: i.custom_id in ["M","F","BI"])
  
  if interacao2.custom_id == "M":
    role = ctx.author.guild.get_role(id_cargo)
    await ctx.author.add_roles(role)
    
   if interacao2.custom_id == "F":
    role2 = ctx.author.guild.get_role(id_cargo)
    await ctx.author.add_roles(role2)
    
   if interacao2.custom_id == "BI":
    role3 = ctx.author.guild.get_role(id_cargo)
    await ctx.author.add_roles(role3)
   
    await interacao2.send(embed=idade, components=[[Button(label=" -18", custom_id="MN", emoji=bot.get_emoji(992689019429343272)),
                                                    Button(label=" +18", custom_id="MR", emoji=bot.get_emoji(992688991876960317)),
                                                    Button(label="Avançar", custom_id="AV", emoji=bot.get_emoji(985174071559979068),style=ButtonStyle.blue, disabled=True),
                                                    Button(label="Voltar", custom_id="VL", emoji=bot.get_emoji(985174071559979068), style=ButtonStyle.red, disabled=True)]])

    interacao3 = await bot.wait_for("button_click", check=lambda i: i.custom_id in ["MN", "MR"])

    if interacao3.custom_id == "MN":
        role4 = ctx.author.guild.get_role(992691097010720798)
        await ctx.author.add_roles(role4)

    if interacao3.custom_id == "MR":
        role5 = ctx.author.guild.get_role(992691011417550960)
        await ctx.author.add_roles(role5)

    stats = discord.Embed(title="Qual é o seu status de relacionamento ?", description="Cargos:\n"
                                                                                       "<@&992704584529235978> <@&992705137653059594> <@&992705344323207290> <@&992705565266554882>",
                          color=0x030303)
    await interacao3.send(embed=stats, components=[[Button(label="Solteiro (a)", custom_id="S", emoji=bot.get_emoji(992707278430031923)),
                                                    Button(label="Enrolado (a)", custom_id="E", emoji=bot.get_emoji(992709413821497385)),
                                                    Button(label="Namorando", custom_id="N", emoji=bot.get_emoji(992707982641074268)),
                                                    Button(label="Casado (a)", custom_id="C", emoji=bot.get_emoji(992710539228745840))],
                                                   [Button(label="Avançar", custom_id="AV", emoji=bot.get_emoji(985174071559979068),style=ButtonStyle.blue, disabled=True),
                                                    Button(label="Voltar", custom_id="VL", emoji=bot.get_emoji(985174071559979068), style=ButtonStyle.red, disabled=True)]])

    interacao4 = await bot.wait_for("button_click", check=lambda i: i.custom_id in ["S", "E", "N", "C"])

    if interacao4.custom_id == "S":
        role6 = ctx.author.guild.get_role(992704584529235978)
        await ctx.author.add_roles(role6)

    if interacao4.custom_id == "E":
        role7 = ctx.author.guild.get_role(992705137653059594)
        await ctx.author.add_roles(role7)

    if interacao4.custom_id == "N":
        role8 = ctx.author.guild.get_role(992705344323207290)
        await ctx.author.add_roles(role8)

    if interacao4.custom_id == "C":
        role9 = ctx.author.guild.get_role(992705565266554882)
        await ctx.author.add_roles(role9)

    regiao = discord.Embed(title="Qual é a sua região ?", description="Cargos: \n"
                                                                      "<@&992720432039997471> <@&992720567855759371> <@&992720605369614366> <@&992720665897619496> <@&992720707089866782> <@&992720761557110864>",
                           color=0x030303)

    await interacao4.send(embed=regiao, components=[[Button(label="Sudeste", custom_id="SU", emoji="↘️"),
                                                     Button(label="Sul", custom_id="SL", emoji="⬇️"),
                                                     Button(label="Centro-Oeste", custom_id="CO", emoji="⏺️"),
                                                     Button(label="Norte", custom_id="NO", emoji="⬆️"),
                                                     Button(label="Nordeste", custom_id="ND", emoji="↗️")],
                                                    [Button(label="Estrangeiro", custom_id="ES", emoji="🌐"),
                                                     Button(label="Avançar", custom_id="AV", emoji=bot.get_emoji(985174071559979068), style=ButtonStyle.blue, disabled=True),
                                                     Button(label="Voltar", custom_id="VL", emoji=bot.get_emoji(985174071559979068), style=ButtonStyle.red, disabled=True)]])

    interacao5 = await bot.wait_for("button_click", check=lambda i: i.custom_id in ["SU", "SL", "CO", "NO", "ND", "ES"])

    if interacao5.custom_id == "SU":
        role10 = ctx.author.guild.get_role(992720432039997471)
        await ctx.author.add_roles(role10)

    if interacao5.custom_id == "SL":
        role11 = ctx.author.guild.get_role(992720567855759371)
        await ctx.author.add_roles(role11)

    if interacao5.custom_id == "CO":
        role12 = ctx.author.guild.get_role(992720605369614366)
        await ctx.author.add_roles(role12)

    if interacao5.custom_id == "NO":
        role13 = ctx.author.guild.get_role(992720665897619496)
        await ctx.author.add_roles(role13)

    if interacao5.custom_id == "ND":
        role14 = ctx.author.guild.get_role(992720707089866782)
        await ctx.author.add_roles(role14)

    if interacao5.custom_id == "ES":
        role15 = ctx.author.guild.get_role(992720761557110864)
        await ctx.author.add_roles(role15)

    fim = discord.Embed(title="<a:certo_:992727485269680188> Registro feito com sucesso!", color=0x030303)
    await interacao5.send(embed=fim)

    
    
bot.run("Token do seu bot")
