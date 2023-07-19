# Filter é um filtro funcional 



def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 01', 'preco': 10.00},
    {'nome': 'Produto 02', 'preco': 20.00},
    {'nome': 'Produto 03', 'preco': 30.00},
    {'nome': 'Produto 04', 'preco': 40.00},
    {'nome': 'Produto 05', 'preco': 50.00}
]

novos_produtos = [
    p for p in produtos
    if p['preco'] > 10
]

novos_produtos2 = filter(
    lambda p: p['preco'] > 38, produtos
)

print_iter(novos_produtos)
print_iter(novos_produtos2)
