lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4]

c= 0
nova_lista = []
for num in lista2:
    soma = int(lista1[c]) + int(lista2[c])
    nova_lista.append(soma)
    c += 1

print(nova_lista)

# Outra forma de fazer

lista_soma = [x + y for x, y in zip(lista1, lista2)]
print(lista_soma)

from itertools import zip_longest
lista_soma2 = [x + y for x, y in zip_longest(lista1, lista2, fillvalue=100)]
print(lista_soma2)
