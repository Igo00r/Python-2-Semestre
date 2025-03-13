x = 'a'
y = 0

# Posso tratar cada exception de uma forma distinta.
try:
    print(f'{x}/{y} = {x/y}')
except ZeroDivisionError:
    print('Não posso fazer x/y pois y = 0')
except TypeError:
    print('Não posso fazer x/y pois têm tipos incompatíveis')
    print(f'x tem tipo {type(x)}')
    print(f'y tem tipo {type(y)}')