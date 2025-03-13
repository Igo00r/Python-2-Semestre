with open('arquivo_texto.txt') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print(linha)