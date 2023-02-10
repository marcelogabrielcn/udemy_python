lista = ['Gabriel', 'Guilherme', 'Gustavo', 'João']
lista.append('Mariazinha')

for indice, nome in enumerate(lista):
    print(indice, nome)


for item in enumerate(lista):  # Irá printar a tupla que cria. 
    print(item)

for item in enumerate(lista):
    for valor in item:
        print(valor)
    
for item in enumerate(lista):  # Exatamente igual a priemira opção
    indice, nome = item
    print(indice, nome)
