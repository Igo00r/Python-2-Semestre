'''
Exercício de organização de código:

Fazer um arquivo primo.py com a função primo, e dar import nesse arquivo
em vez de precisar dar ctrl+c ctrl+v na função.
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
'''
def mostra_primos(inicio, fim = None, tamanho = 100):
    # se o fim não foi fornecido, calculo como sendo inicio + tamanho
    if fim is None:
        fim = inicio + tamanho
    for i in range(inicio, fim):
        if primo(i):
            print(i)

# nessa chamada, fica implícito que o 40 é o "fim" pois é o segundo parâmetro
mostra_primos(15, 40)
print()

# preciso nomear o parâmetro "tamanho" senão seria suposto que 50 é o "fim"
mostra_primos(100, tamanho = 50)
print()

# por clareza, é legal usar parâmetros nomeados mesmo quando não obrigatório
# na linha logo abaixo, não precisaria nomear nenhum dos parâmetros
mostra_primos(inicio = 15, fim = 40)

print()

# na linha logo abaixo, não precisaria nomear o parâmetro inicio
mostra_primos(inicio = int(1e7), tamanho = 200)