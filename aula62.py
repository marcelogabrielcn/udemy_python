lista = [
    {'nome': 'Gabriel', 'sobrenome': 'Ferreira'},
    {'nome': 'Larissa', 'sobrenome': 'Marques'},
    {'nome': 'Daniel', 'sobrenome': 'Sousa'},
    {'nome': 'Rosa', 'sobrenome': 'Maria'},
    {'nome': 'Mateus', 'sobrenome': 'Oliveira'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
