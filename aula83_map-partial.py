# Map - Para mapear dados 
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 1', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 23.92},
    {'nome': 'Produto 3', 'preco': 92.94},
    {'nome': 'Produto 4', 'preco': 1104.92},
    {'nome': 'Produto 5', 'preco': 2014.02},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

novos_produtos = [
    {**p, 'preco': aumentar_porcentagem(p['preco'], 1.1)} for p in produtos  # Isso se chama list comprehension, tenho que pesquisar mais a fundo
]

print_iter(produtos)
print_iter(novos_produtos)

