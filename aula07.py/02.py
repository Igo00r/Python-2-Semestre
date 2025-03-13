# Baseado no 04.py da aula passada

import json

with open('members.json') as arquivo:
    membros = json.load(arquivo)

# nomes de todos os membros que estão  listados no arquivo
nomes_membros = [ membro['ParliamentaryName'] for membro in membros ]

nomes_membros.sort()
print('Nomes de todas as pessoas listadas no arquivo, em ordem alfabética:')
for nome in nomes_membros:
    print(nome)

'''
Exercício: criar lista com nomes de membros cujo atributo "IsCurrent" seja False

('IsCurrent' marca se a pessoa é atualmente congressista ou não)
'''
nomes_membros_inativos = []
nomes_membros_ativos = []
for membro in membros:
    nome = membro['ParliamentaryName']
    if membro['IsCurrent']: # esse campo tem valor True ou False
        nomes_membros_ativos.append(nome)
    else:
        nomes_membros_inativos.append(nome)

print('')
print('Nomes de membros atuais (em exercício):')
nomes_membros_ativos.sort()
for nome in nomes_membros_ativos:
    print(nome)