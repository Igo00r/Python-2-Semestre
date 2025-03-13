'''
Este programa lê um número inteiro e determina se ele é
positivo, negativo, ou zero.
'''

numero = int(input())
if numero > 0:
    print('O número é positivo')
elif numero == 0:
    print('O número é zero')
else:
    print('O número é negativo')