'''
Exercício:

Parte 1: modifique 02.py para que o câmbio seja a partir do EUR
em vez de USD.

(Resolvido abaixo)

Parte 2: modifique para que o usuário escolha a moeda de
origem e a moeda alvo do câmbio.

(Vamos fazer para resolver na aula amanhã)
'''

import requests

# ideia principal: quebrar a URL entre a base e a parte que especifica uma moeda
base_url = 'https://api.exchangerate-api.com/v4/latest/'
moeda_origem = 'EUR'

url = base_url + moeda_origem

resposta = requests.get(url)

# por simplicidade do código vou supor que o GET foi bem sucedido
cambio = resposta.json()

print(f'Cambio do {moeda_origem} da seguinte data: {cambio['date']}')
print('Qual a moeda alvo? Digite o codigo com tres letras')
print('Exemplo: real = BRL, libra = GBP, peso argentino = ARS')

moeda_alvo = input()
print(f'1 {moeda_origem} = {cambio['rates'][moeda_alvo]} {moeda_alvo}')
