import requests_html
import requests
import telebot
import re
import json
import random
import string
from random import *
from time import sleep


bot = telebot.TeleBot("5055232832:AAHBGOOMubkPca2hRqx3Lw2YmI5ozmInOcQ")


@bot.message_handler(commands=['start'] + ['menu'])
def bniio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/menuu':
        bot.reply_to(
            men, '<b>' + 'Verifique se o comando foi digitado corretamente.' + '</b>', parse_mode='HTML')
    else:
        try:
            bot.reply_to(men, '<b>' '🔍 MENU DE COMANDOS:' '</b>' + '\n\n' +
                         '<b>' '📌[✓] CPF:</b><code> /cpf 94039038720' '</code>' + '\n\n' + '<b>' '📌[✓] CEP:</b><code> /cep 01001000' '</code>' + '\n\n' + '<b>👥 BY: https://paineldeconsulta.xyz/</b>', parse_mode='HTML')
        except:
            bot.reply_to(men, '<b>' + '.' + '</b>', parse_mode='HTML')
##


@bot.message_handler(commands=['cpf'] + ['CPF'])
def bno(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    bot.reply_to(men, 'Pesquisando...')
    if men.text == '/cpf':
        bot.reply_to(men, '<b>' + 'Digite um CPF.' + '</b>', parse_mode='HTML')
    if men.text == '/CPF':
        bot.reply_to(men, '<b>' + 'Digite um CPF' + '</b>', parse_mode='HTML')
    else:
        try:
            ipp = re.sub('[^0-9]', '', mensagem)
            url = requests.get(
                'Alugue a sua api de cpf | contato@paineldeconsulta.xyz' + ipp)
            reqi = url.json
            bot.reply_to(men, '<b>' '✅ | CPF ENCONTRADO' '</b>' + '\n============================\n\n' + '<b>' 'Nome: ' '</b>' '<code>' + reqi()['nome'] + '</code>' '\n' + '<b>' 'Nascimento: ' '</b>' '<code>' + reqi()['nascimento'] + '</code>' '\n' + '<b>' 'CPF: ' '</b>' '<code>' + reqi()['cpf'] + '</code>' '\n' + '<b>' 'CNS: ' '</b>' '<code>' + reqi()['cns'] + '</code>' '\n\n' + '<b>' 'Mãe: ' '</b>' '<code>' + reqi()['mae'] + '</code>' '\n' + '<b>' 'Pai: ' '</b>' '<code>' + reqi()[
                         'pai'] + '</code>' '\n\n' + '<b>' 'RG: ' '</b>' '<code>' + reqi()['numeroDoRg'] + '</code>' '\n' + '<b>' 'Orgão: ' '</b>' '<code>' + reqi()['orgaoEmissor'] + '</code>' '\n' + '<b>' 'RG-UF: ' '</b>' '<code>' + reqi()['estadoDoRg'] + '</code>' '\n' + '<b>' 'Emissão: ' '</b>' '<code>' + reqi()['dataDeEmissaoDoRg'] + '</code>' '\n\n' + '<b>' 'Cidade: ' '</b>' '<code>' + reqi()['municipio'] + '</code>' '\n' + '<b>' 'Bairro: ' '</b>' '<code>' + reqi()['bairro'] + '</code>' '\n' + '<b>' 'Logradouro: ' '</b>' '<code>' + reqi()['logradouro'] + '</code>' '\n' + '<b>' 'Numero: ' '</b>' '<code>' + reqi()['numero'] + '</code>' '\n' + '<b>' 'CEP: ' '</b>' '<code>' + reqi()['cep'] + '</code>' '\n\n============================\n', parse_mode='HTML')
            print('CPF: '+ ipp +' Encontrado.')
        except:
            bot.reply_to(men, '<b>' + 'CPF Não encontrado.' +
                         '</b>', parse_mode='HTML')
            print('CPF: '+ ipp + ' Não encontrado.')


##


@bot.message_handler(commands=['cep'] + ['CEP'])
def bno(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    bot.reply_to(men, 'Pesquisando...')
    if men.text == '/cep':
        bot.reply_to(men, '<b>' + 'Digite um CEP.' + '</b>', parse_mode='HTML')
    if men.text == '/CEP':
        bot.reply_to(men, '<b>' + 'Digite um CEP' + '</b>', parse_mode='HTML')
    else:
        try:
            ipp = re.sub('[^0-9]', '', mensagem)
            url = requests.get(
                'https://viacep.com.br/ws/' + ipp + '/json/')
            reqi = url.json
            bot.reply_to(men, '<b>' '✅ | CEP ENCONTRADO' '</b>' + '\n============================\n\n' + '<b>' 'CEP: ' '</b>' '<code>' + reqi()['cep'] + '</code>' '\n' + '<b>' 'Logradouro: ' '</b>' '<code>' + reqi()['logradouro'] + '</code>' '\n' + '<b>' 'Complemento: ' '</b>' '<code>' + reqi()['complemento'] + '</code>' '\n' + '<b>' 'Bairro: ' '</b>' '<code>' + reqi()['bairro'] + '</code>' '\n' + '<b>' 'Localidade: ' '</b>' '<code>' + reqi()['localidade'] + '</code>' '\n' + '<b>' 'UF: ' '</b>' '<code>' + reqi()[
                         'uf'] + '</code>' '\n' + '<b>' 'IBGE: ' '</b>' '<code>' + reqi()['ibge'] + '</code>' '\n' + '<b>' 'GIA: ' '</b>' '<code>' + reqi()['gia'] + '</code>' '\n' + '<b>' 'DDD: ' '</b>' '<code>' + reqi()['ddd'] + '</code>' '\n' + '<b>' 'Siafi: ' '</b>' '<code>' + reqi()['siafi'] + '</code>' '\n\n============================\n', parse_mode='HTML')
            print('CEP: '+ ipp +' Encontrado.')
        except:
            bot.reply_to(men, '<b>' + 'CEP Não encontrado.' +
                         '</b>', parse_mode='HTML')
            print('CEP: '+ ipp + ' Não encontrado.')


bot.infinity_polling()
