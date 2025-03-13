valores = [ 3, 10, -6, 8, 47, 0, 5, 11, 9 ]

menores_que_10 = [ valor for valor in valores if valor < 10 ]
print(menores_que_10)

# A linha é equivalente a montar com append:
menores_que_10 = []
for valor in valores:
    if valor < 10:
        menores_que_10.append(valor)

'''
O método da linha 3 se chama "compreensão de lista" ou "list comprehension"
e é uma forma mais compacta de fazer essa tarefa que é bastante comum:
selecionar apenas os dados que passam por algum filtro.
'''

# Não precisa ser um filtro simples, posso aplicar mais lógica / transformações
dobro_dos_menores_que_10 = [ 2*valor for valor in valores if valor < 10 ]
print(dobro_dos_menores_que_10)


'''
Exercício: reveja com calma exemplos 03.py e 04.py
'''