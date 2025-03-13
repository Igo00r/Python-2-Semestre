'''
Este programa lê dois inteiros e imprime "ok"
se ambos são ímpares.
'''

num1 = int(input())
num2 = int(input())

# se num1 é ímpar e num2 é ímpar, imprimo ok
if num1 % 2 == 1 and num2 % 2 == 1:
    print('ok')

'''
Obs.: também podemos verificar assim:

if num1*num2 % 2 == 1:
    print('ok')

(Pois o produto entre os dois é ímpar só se ambos são ímpares)
'''