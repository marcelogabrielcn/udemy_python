lista1 = ['Marcelo', 'Gabriel', 'João']
lista2 = lista1
print(lista1)
print(lista2)

lista1[1] = 'Fernando'  # Quando uso "=" ele cria uma dependencia dos endereços de mem.
print(lista1)
print(lista2)

lista3 = lista1.copy()  # Copy copia apenas o valor, não associa ao endereço
print(lista1)
print(lista3)

lista1[2] = 'Mariazinha'
print(lista1)
print(lista3)
