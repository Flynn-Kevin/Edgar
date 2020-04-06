import discord
import datetime
# import socket
import requests
import os
import identidade as idnt
import funcoes as func
import funcoes_privadas as funcp


cliente = discord.Client()
tempo0 = datetime.datetime.now() - datetime.timedelta(hours=12)
tempo1 = tempo0
tempo_espera = datetime.timedelta(hours=2)
# cliente_de_voz = 0
# discord.opus.load_opus('/usr/lib/x86_64-linux-gnu/libopus.so.0')
@cliente.event
async def on_ready():
    print(f'We have logged in as {cliente.user}')
    # print(cliente.user.mention)
    print(cliente.user.display_name)
    # print(cliente.user.discriminator)
    for guild in cliente.guilds:
        for channel in guild.channels:
            if str(channel) == 'geral':
                print(f'{guild} - {channel}')
                break
    # await channel.send('cheguei')
@cliente.event
async def on_message(message):

    if message.author == cliente.user:
        return

    nao_respondido = 1

    if not (func.palavras_in_mensagem_and([cliente.user.display_name.lower()], message.content.lower())):
        return

    print(f'mensagem: {message.content}')
    print(f'canal: {message.channel}')
    print(f'autor: {message.author}')
    print(f'guild: {message.guild}')

    if func.palavras_in_mensagem_or(['olá', 'ola'], message.content.lower()):
        print(f'{message.author.mention} Alow!')
        await message.channel.send(f'{message.author.mention} Alow!')
        nao_respondido = 0

    if func.palavras_in_mensagem_and(['que', 'dia', 'hoje', '?'], message.content.lower()):
        print(f'Hoje é {datetime.datetime.now().strftime("%d/%m/%Y")}')
        Data = func.retorna_data(datetime.datetime.now())
        print(f'Hoje é dia {Data}.')
        await message.channel.send(f'Hoje é dia {Data}.')
        nao_respondido = 0

    if func.palavras_in_mensagem_and(['que', 'horas', '?'], message.content.lower()):
        print(f'São {datetime.datetime.now().strftime("%H horas e %M minutos.")}')
        await message.channel.send(f'São {datetime.datetime.now().strftime("%H horas e %M minutos.")}')
        nao_respondido = 0

    if func.palavras_in_mensagem_and(['obrigado'], message.content.lower()):
        resposta = (f'Por nada!')
        print(resposta)
        await message.channel.send(resposta)
        nao_respondido = 0

    if func.palavras_in_mensagem_or(['esperto', 'simpático', 'inteligente', 'bonito', 'elegante'], message.content.lower()):
        resposta=(f'Obrigado {message.author.mention}!')
        print(resposta)
        await message.channel.send(resposta)
        nao_respondido = 0

    if func.palavras_in_mensagem_and(['qual', 'ip', '?'], message.content.lower()):
        if str(message.author) == idnt.mestre:
            ipaddr = requests.get('https://api.ipify.org').text
            await message.channel.send(f'Meu IP é {ipaddr}')
            print(f'Meu IP é {ipaddr}')
            nao_respondido = 0

    if message.content.lower().startswith('executar comando: '):
        print(f'mensagem: {message.content}')
        if str(message.author) == idnt.mestre:
            comando = message.content[18:]
            stream = os.popen(comando)
            output = stream.read()
            print(output)
            await message.channel.send(output)
            nao_respondido = 0

    if func.palavras_in_mensagem_and(['teste', 'boas', 'vindas'], message.content.lower()):
        member = message.author
        channel = func.retorna_canal_by_str_guild_channel(cliente, str(member.guild), "testebot")
        await channel.send(funcp.mensagem_boas_vindas(member))
        nao_respondido = 0

    if nao_respondido:
        global tempo0, tempo1
        tempo1 = datetime.datetime.now()
        if (tempo1 - tempo0) > tempo_espera:
            tempo0 = tempo1
            channel = message.channel
            await channel.send('Tem alguém falando de mim! \nCom certeza é algo bom!')


@cliente.event
async def on_member_join(member):
    # channel = func.retorna_canal_by_str_guild_channel(cliente, str(member.guild), "geral")
    # await channel.send(funcp.mensagem_boas_vindas(member))
    print(funcp.mensagem_boas_vindas(member))

@cliente.event
async def on_member_update(antes, member):
    cargos = funcp.retorna_cargos(member.guild)
    com_cargo_antes = False
    ganhou_cargo = False
    for role in antes.roles:
        if str(role) in cargos:
            com_cargo_antes = True
            break
    if not com_cargo_antes:
        for role in member.roles:
            if str(role) in cargos:
                ganhou_cargo = True
                break
    if ganhou_cargo:
        channel = func.retorna_canal_by_str_guild_channel(cliente, str(member.guild), "geral")
        await channel.send(funcp.mensagem_boas_vindas(member))


cliente.run(idnt.TOKEN)
