'''
Recebe um número n e devolve:
    True, se é número primo;
    False caso contrário.
'''
def primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0: # se não é 2 mas é par, então não é primo
        return False
    
    # vou testar apenas divisores ímpares! Já testei se o número é par.
    for possivel_divisor in range(3, n, 2):
        if n % possivel_divisor == 0:
            # encontrei divisor de n. Então n não é primo
            return False
    return True

'''
Mostra os números primos em um intervalo numérico.

Recebe o início do intervalo e o tamanho do intervalo.
O intervalo tem tamanho 100 por padrão. (Portanto é parâmetro opcional!)
'''
def mostra_primos(inicio, tamanho = 100):
    fim = inicio + tamanho
    for i in range(inicio, fim):
        if primo(i):
            print(i)

# 1 milhão até 1 milhão e 100
mostra_primos(1000000, 200)

# 10 milhões até 10 milhões e 100
mostra_primos(int(1e7))

# 20 milhões até 20 milhões e 100
mostra_primos(int(2e7))

'''
Exercício:

    (a) Altere a função para receber, em vez de inicio e fim do intervalo,
    receber o inicio e o TAMANHO do intervalo

    (b) Altere a função para que o intervalo seja um parâmetro opcional
    com valor padrão igual a 100.
'''