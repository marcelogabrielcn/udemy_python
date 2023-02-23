# List comprehension, é uma forma de criar algumas coisas de forma mais "simples" ex.

lista = []
for numero in range(10):
    lista.append(numero)

print(lista)

lista2 = [numero * 2 for numero in range(10)]
#         operação   para cada valor em um range

print(lista2)
