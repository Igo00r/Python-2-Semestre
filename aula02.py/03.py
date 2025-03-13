import json

with open('members.json') as arquivo:
    membros = json.load(arquivo)

# print(membros)
nomes_membros = []
for membro in membros:
    nomes_membros.append(membro['ParliamentaryName'])

# print(nomes_membros)
# Exercício: imprimir em ordem alfabética, um por linha
nomes_membros.sort()
for nome in nomes_membros:
    print(nome)