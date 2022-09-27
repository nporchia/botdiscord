import discord
from discord.ext import commands, tasks
from discord.utils import get
import asyncio
import random
import datetime
import pymongo
from pymongo import MongoClient


client = discord.Client()
client = commands.Bot(command_prefix="/")
client.remove_command('help')

miembros_vip=[758553031553450005,758366411956813824,719364591791898707,750160101654003712,765326250033152021,770091394647719936,766727483776041009,762091417249644594]
#             hype dev            hype BOT          Panteon khorthenio     Hype Gaming    Hype Among us         Hype CSGO       Hype Programmer
players = {}
now = datetime.datetime.now()


@client.event
async def on_ready():
    contador=0
    for serv in client.guilds:
        contador=contador+1
    estado="Actualmente en:",len(client.guilds),"Servidores"
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("||HYPE||"))
    print('Me conecte con el nombre de {0.user}'.format(client))
    eliminarprivadosinactivos.start()

@tasks.loop(seconds=5)
async def eliminarprivadosinactivos():
    dia=now.day
    mes=now.month
    #print("Dia:",dia,"Mes",mes)
    cluster = pymongo.MongoClient("mongodb+srv://hypegaming:SUSANA18@cluster0.00h5l.mongodb.net/Hype?retryWrites=true&w=majority")
    db = cluster["hype"]
    collection=db["cumpleaños"]
    results = collection.find({"Dia":f"{dia}","Mes":f"{mes}"})
    lista1=[]
    for result in results:
        lista1.append(result["Nombre"])
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.name=="recordatoriocumpleaños" and guild.id==834211160534286406:
                for cumpleañero in lista1:
                    await channel.send(f" 📢 **Hoy cumple:** {cumpleañero} 👏👏👏")


@client.event
async def on_voice_state_update(member, before, after):
    idcanal=0
    try:
        idcanal=after.channel.id
    except:
        idcanal=0
    if idcanal==765461524696924180:
        for server in client.guilds:
            if server.id==750160101654003712:
                for categoria in server.categories:
                    if categoria.id==765461523950469140:
                        lacategoria=categoria
                        break
                canal="🔒│"+" "+'Privada'' '+ member.name
                overwrites = {server.default_role: discord.PermissionOverwrite(connect=True)}
                channel=await server.create_voice_channel(name=canal,category=lacategoria,overwrites=overwrites)
                await channel.set_permissions(member,connect=True)
                await member.move_to(channel)
                Nombre='Privada de ' + member.name
    #? Among Us
    if idcanal==779466692693983243:
        for server in client.guilds:
            if server.id==750160101654003712:
                guild=server
                role = get(member.guild.roles, id=779445907912523787)
                role3 = get(member.guild.roles, id=779449541275156520)
                try:
                    await member.add_roles(role,role3)
                    await member.send("**Se te entrego el rol Among Us, Recuerda leer las reglas!**")
                except:
                    pass
    #? Programacion
    if idcanal==779466964212645928:
        for server in client.guilds:
            if server.id==750160101654003712:
                guild=server
                role = get(member.guild.roles, id=779446020504813598)
                role3 = get(member.guild.roles, id=779449541275156520)
                try:
                    await member.add_roles(role,role3)
                    await member.send("**Se te entrego el rol Programmer, Recuerda leer las reglas!**")
                except:
                    pass
    #? Comunidad
    if idcanal==779466887532773406:
        for server in client.guilds:
            if server.id==750160101654003712:
                guild=server
                role = get(member.guild.roles, id=750168150871506985)
                role3 = get(member.guild.roles, id=779449541275156520)
                try:
                    await member.add_roles(role,role3)
                    await member.send("**Se te entrego el rol Comunidad, Recuerda leer las reglas!**")
                except:
                    pass

@client.command()
async def fichar(ctx):
    await ctx.message.delete()
    await ctx.send(datetime.datetime.now())
@client.command()
async def privbloquear(ctx,rol:discord.Role,member:discord.Member):
    await ctx.message.delete()
    if ctx.guild.id==750160101654003712 and ctx.author.name in rol.name:
        await member.remove_roles(rol)
#errores
@client.event
async def on_command_error(ctx,error):
    if isinstance(error, discord.Forbidden):
        print('Error padreeeeeee hablale a ken_3#0001')
    if isinstance(error, commands.CommandNotFound):
        pass
@client.command()
async def localizar(ctx,member: discord.Member):
    await ctx.message.delete()
    voicechannel=member.voice.channel
    await ctx.send(f"**El canal es:**{voicechannel.name}")
@client.command()
async def ticket(ctx,numero=0):
    author=ctx.author
    await ctx.message.delete()
    canal="🔱│"+'ticket'' '+author.name
    guild=ctx.guild
    overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False,send_messages=False)}
    if numero==0:
        channel=await guild.create_text_channel(name=canal,overwrites=overwrites)
        for role in guild.roles:
            if role.name=="Soporte":
                await channel.set_permissions(role,read_messages=True,send_messages=True)
        await channel.set_permissions(author,read_messages=True,send_messages=True)
        ctx=channel
        await ctx.send(f'**Espera, un staff va a ver tu ticket**{author.mention}    @everyone')
        await ctx.send('**Para cerrar tu ticket usa /cerrarticket**')
    elif numero==1:
        canal="🚪│"+'ticket'' '+author.name
        channel=await guild.create_text_channel(name=canal,overwrites=overwrites)
        await channel.set_permissions(author,read_messages=True,send_messages=True)
        ctx=channel
        await ctx.send(f'**Espera, Cualquier Dueño o Staff rango alto va a ver esto**{author.mention}    @everyone')
@client.command()
async def tomarticket(ctx):
    if ctx.guild.id in miembros_vip:
        await ctx.message.delete()
        for role in ctx.author.roles:
            if role.name=='Soporte':
                for role in ctx.guild.roles:
                    if role.name=="Soporte":
                        await ctx.send(f"**El STAFF {ctx.author.mention} se encargara del reporte**")
                        await ctx.channel.set_permissions(role,read_messages=True,
                                                                send_messages=False)
                        await ctx.channel.set_permissions(ctx.author,read_messages=True,
                                                                    send_messages=True)
                        break
@client.command()
async def cerrarticket(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        if role.name=='Soporte':
            rolsoporte=role
            break
    for canal in ctx.guild.channels:
        if canal.name[0:8]=='🔱│ticket' and ctx.channel.id==canal.id:
            await canal.edit(name="🔱│ticket cerrado")
            await ctx.send(f"**🔒{ctx.author.mention} Ha cerrado el ticket🔒 **")
            for member in ctx.channel.members:
                await ctx.channel.set_permissions(member,read_messages=True,
                                                    send_messages=False)
            await ctx.channel.set_permission(rolsoporte,read_messages=True,
                                                        send_messages=False)
@client.command()
@commands.has_permissions(manage_messages=True)
async def limpiar(ctx,amount=3):
    await ctx.channel.purge(limit=(amount+1))
    await ctx.send("``` Borre {} mensajes  ```" .format(amount))
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=1)
#! *********************************************************************************************************************************************************************
@client.command()
@commands.has_permissions(kick_members=True)
async def advertir(ctx,member:discord.Member,*,texto='NO DATA ENTERED'):
    await ctx.message.delete()
    if texto=='NO DATA ENTERED':
        await ctx.send("**Advertencia?**")
    elif texto!='NO DATA ENTERED':
        cluster = pymongo.MongoClient("mongodb+srv://hypegaming:SUSANA18@cluster0.00h5l.mongodb.net/Hype?retryWrites=true&w=majority")
        db = cluster["hype"]
        collection=db["advertencias"]
        guildid=ctx.guild.id
        post= {"idusuario":member.id,"Advertencia":texto}
        collection.insert_one(post)
        #TODO -EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!-
        embed= discord.Embed(
            colour=discord.Colour.from_rgb(229,255,0)
            )
        embed.set_author(name="HYPE Moderacion",url="https://hypegaming.com.ar",icon_url="https://cdn.discordapp.com/attachments/743970465499840563/757694287826649128/Diversion-Recuperado.jpg")
        embed.add_field(name="**Un Usuario Ha Sido Advertido:**",value=member.mention,inline=True)
        embed.add_field(name="**ADVERTENCIA::**",value=texto,inline=False)
        await ctx.send(embed=embed)
        advertidor=ctx.author
        try:
            await member.send(f"Has sido advertido en Hype, Advertencia:{texto}")
        except:
            pass
        for channel in ctx.guild.channels:
            if 'auditoria' in channel.name:
                ctx=channel
                await ctx.send("**El usuario : {} ha sido Advertido por:{}**` {} `".format(member.mention,advertidor.mention,texto))
    else:
        print("ERROR")
#! *********************************************************************************************************************************************************************
@client.command()
async def advertencias(ctx,member:discord.Member):
    await ctx.message.delete()
    cluster = pymongo.MongoClient("mongodb+srv://hypegaming:SUSANA18@cluster0.00h5l.mongodb.net/Hype?retryWrites=true&w=majority")
    db = cluster["hype"]
    collection=db["advertencias"]
    guildid=ctx.guild.id
    results = collection.find({"idusuario":member.id})
    lista=[]
    for result in results:
        lista.append(result["Advertencia"])
    #TODO -EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!--EMBED!-
    embed= discord.Embed(
        title='Info del Usuario/User Info',
        colour=discord.Colour.from_rgb(229,255,0)
    )
    elmiembro=member.name
    embed.set_author(name=elmiembro)
    nombre=ctx.guild.name
    if len(lista)==0:
        embed.add_field(name='Advertencia:',value='No tiene advertencias')
        
    else:
        for i in range(len(lista)):
            premio=lista[i]
            embed.add_field(name='Advertencia:',value=premio, inline=False)
    embed.set_author(name="HYPE",url="https://hypegaming.com.ar",icon_url="https://cdn.discordapp.com/attachments/743970465499840563/757694287826649128/Diversion-Recuperado.jpg")
    embed.set_footer(text=nombre, icon_url="https://cdn.discordapp.com/attachments/743970465499840563/757694287826649128/Diversion-Recuperado.jpg")
    await ctx.send(embed=embed)
#! *********************************************************************************************************************************************************************
@client.command()
@commands.has_permissions(administrator=True)
async def eliminaradvertencias(ctx,member:discord.Member):
    cluster = pymongo.MongoClient("mongodb+srv://hypegaming:SUSANA18@cluster0.00h5l.mongodb.net/Hype?retryWrites=true&w=majority")
    db = cluster["hype"]
    collection=db["advertencias"]
    guildid=ctx.guild.id
    collection.delete_many({"idusuario":member.id})
    await ctx.send("**Advertencias Eliminadas**")
#! *********************************************************************************************************************************************************************
#auditoria
@client.event
async def on_member_ban(guild, user):
    for channel in guild.channels:
        if 'auditoria' in channel.name or 'auditoría' in channel.name:
            ctx=channel
            await ctx.send(""" El usuario {} Fue baneado """.format(user.mention))
@client.event
async def on_member_unban(guild, user):
    for channel in guild.channels:
        if 'auditoria' in channel.name or 'auditoría' in channel.name:
            ctx=channel
            await ctx.send(""" El usuario {} Fue desbaneado """.format(user.mention))

client.run('NzYwMDE0MjU5OTgzNDgyOTEw.X3F4bw.POczkU5fNSYyBBcOSCjSg_63LTM')
