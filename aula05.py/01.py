'''
Recebe um número n e devolve:
    True, se é número primo;
    False caso contrário.
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
Vamos procurar primos maiores.
Começando por volta de 1 milhão.
'''
inicio = 1000000
fim = inicio + 100
for i in range(inicio, fim):
    if primo(i):
        print(i)

# agora perto de 10 milhões
inicio = int(1e7)   # 1*10^7 (10 milhões)
fim = inicio + 100
for i in range(inicio, fim):
    if primo(i):
        print(i)

'''
Exercício:

    (a) Execute um for como os acima para o intervalo começando em 20 milhões
    (b) Observe o tempo de exeução (a olho nu, o tempo que demora para printar)
    (c) Defina uma função que recebe "inicio" e "fim" e realiza um for como os acima.
'''