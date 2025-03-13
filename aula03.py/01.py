'''
fonte do JSON : https://api.exchangerate-api.com/v4/latest/USD

Taxas de câmbio atualizadas do USD para as outras moedas.

(Obs.: trocando "USD" por outra moeda na URL, dá para pegar taxas de
câmbio a partir dessa outra moeda.)

Exercício para próxima aula: programa acessar link em vez de baixar
o JSON manualmente!
'''

import json

with open('cambio-usd.json') as arquivo:
    cambio = json.load(arquivo)

print('Cambio do dolar (USD) da seguinte data:', cambio['date'])
print('Qual a moeda alvo? Digite o codigo com tres letras')
print('Exemplo: real = BRL, libra = GBP, peso argentino = ARS')

moeda_desejada = input()
print('1 USD = ', cambio['rates'][moeda_desejada], moeda_desejada)