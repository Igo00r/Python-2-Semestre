import json

with open('cambio_usd.json') as arquivo:
    dicionario_cambio = json.load(arquivo)

# o campo rates traz todas as taxas de câmbio de quanto vale 1 USD em outras moedas
taxas = dicionario_cambio['rates']

# print(taxas)
'''
Exercício: construir uma lista das moedas que valem mais do que o USD.
Ou seja, aquelas moedas tais que 1 USD vale menos do que 1 dessa meoda.
'''
moedas_fortes = []
# vamos percorrer todas as chaves do dicionário, que são as diferentes moedas
for moeda in taxas:
    if taxas[moeda] < 1:
        moedas_fortes.append(moeda)

print('Lista de moedas que valem mais do que USD:')
for moeda in moedas_fortes:
    print(moeda)

quantidade_moedas = len(taxas)
quantidade_moedas_fortes = len(moedas_fortes)
proporcao_fortes = quantidade_moedas_fortes/quantidade_moedas

print(f'Das moedas com taxa de câmbio disponível {proporcao_fortes*100}% valem mais do que o USD')