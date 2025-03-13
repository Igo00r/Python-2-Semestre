# Baseado no arquivo 03.py da aula passada

temperaturas = []
with open('dados.txt') as arquivo:
    for linha in arquivo:
        temperaturas.append(float(linha))

print(f'Eu montei a lista com todas as {len(temperaturas)} temperaturas.')

'''
# construção "tradicional", sem compreensão de lista
temperaturas_altas = []
for temp in temperaturas:
    if temp > 90:
        temperaturas_altas.append(temp)
'''

# construção equivalente com compreensão de lista
temperaturas_altas = [ temp for temp in temperaturas if temp > 90 ]

print(f'Destas, {len(temperaturas_altas)} são altas (acima de 90C).')

proporcao_altas = len(temperaturas_altas)/len(temperaturas)
print(proporcao_altas)

# EXERCÍCIO (agora): Printar a proporção de temperaturas altas na forma de porcentagem

'''
Exercício (da aula passada): crie (usando compreensão de lista):
    (a) temperaturas_altas, contendo as temperaturas acima de 90

    (b) temperaturas_muito_altas, contendo as temperaturas acima de 100

    (c) Depois vamos ver o tamanho dessas listas comparadas com a lista total
de temperaturas, para ver qual proporção do tempo está em temperatura alta
'''
