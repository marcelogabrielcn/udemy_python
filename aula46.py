def soma(x, y, z=None):  #None é tipo "sem valor" o que é diferente de 0... pois 0 é um valor.
    if z is not None:
        print(f'Soma de {x} + {y} + {z} = ', x + y + z)
    else:
        print(f'Soma de {x} + {y} = ', x + y)



soma(2, 4)
soma(6, 3)
soma(4, 45, 0)
