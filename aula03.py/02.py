'''

Igual ao exemplo 1, porém acessando os dados por request.
Ou seja, nosso programa vai acessar o servidor diretamente
para tentar pegar o JSON mais recente possível.
'''

import requests

url = 'https://api.exchangerate-api.com/v4/latest/USD'

# faz uma requisição à URL e salva a resposta do servidor
resposta = requests.get(url)

# a resposta é 200 se tiver dado certo
if resposta.status_code == 200:
    cambio = resposta.json()
else:
    print('Falha em acessar o servidor com os dados. Terminando...')
    exit() # termina o programa


# restante da lógica é idêntica ao programa 01.py
print('Cambio do dolar (USD) da seguinte data:', cambio['date'])
print('Qual a moeda alvo? Digite o codigo com tres letras')
print('Exemplo: real = BRL, libra = GBP, peso argentino = ARS')

moeda_desejada = input()
print('1 USD = ', cambio['rates'][moeda_desejada], moeda_desejada)