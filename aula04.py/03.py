'''
Recebe um número n e devolve True, se é número primo; False caso contrário.

Um número n é primo se é divisível APENAS por 1 e por n, ou seja,
se não tem outros divisores.
'''
def primo(n):
    if n <= 1:
        return False
    for possivel_divisor in range(2, n):
        if n % possivel_divisor == 0:
            # encontrei divisor de n. Então n não é primo
            return False
    return True

'''
Exercício: faça um programa que printa, dentre os números de
1 até 100, apenas aqueles que são primos.
'''

for i in range(1, 100):
    if primo(i):
        print(i)

'''
Exercício: use a função "primo" para encontrar algum número primo
maior do que 10 milhões.
'''

# resultado = primo(2)
# print('2 é primo?', resultado)

# resultado = primo(5)
# print('5 é primo?', resultado)

# resultado = primo(27)
# print('27 é primo?', resultado)