# import discord
# import datetime
# # import socket
# import requests
# import os
# import identidade as idnt


def palavras_in_mensagem_and(lista_palavras, mensagem):
    saida=True
    for palavra in lista_palavras:
        if palavra in mensagem:
            saida=True and saida
        else:
            saida=False
            break
    return saida


def palavras_in_mensagem_or(lista_palavras, mensagem):
    saida=False
    for palavra in lista_palavras:
        if palavra in mensagem:
            saida=True
            break
    return saida


def retorna_data(data):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    dias_da_semana = ['a segunda-feira', 'a terça-feira', 'a quarta-feira',
                      'a quinta-feira', 'a sexta-feira', ' sábado', ' domingo']
    data_ex = f'{data.day} de {meses[data.month]} de {data.year},\n' \
              f'um{dias_da_semana[data.weekday()]}'
    return data_ex


def retorna_canal_by_str_guild_channel(cliente, procura_guild, procura_channel):
    for guild in cliente.guilds:
        for channel in guild.channels:
            if str(guild) == procura_guild:
                if str(channel) == procura_channel:
                    return channel


def retorna_usuarios(cliente):
    for guild in cliente.guilds:
        for member in guild.members:
            print(f'name {member.name} mention {member.mention}')



