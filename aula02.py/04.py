import json

with open('membros_grupo.json') as arquivo:
    membros = json.load(arquivo)

nomes = [ membro["Nome"] for membro in membros ]
print(nomes)