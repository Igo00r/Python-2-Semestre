'''
Usa input para ler um float.
Enquanto a entrada não for válida, imprime uma mensagem de erro e tenta novamente.
'''
def le_float():
    bem_sucedido = False
    while not bem_sucedido:
        try: 
            entrada = float(input())
            bem_sucedido = True
            # cada linha do bloco "try" só é executada se a anterior não levantou exception
        except:
            print('Valor inválido. Por favor digite um número.')
    
    return entrada


print('Digite dois números:')
x = le_float()
y = le_float()

print(f'{x} + {y} = {x+y}')

try:
    print(f'{x}/{y} = {x/y}')
except:
    print('Não vou mostrar a divisão x/y pois y = 0')
