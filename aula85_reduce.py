# Reduce - faz a redução de um iveterável em um valor 

from functools import reduce

produtos = [
    {'nome': 'Produto 01', 'preco': 10.00},
    {'nome': 'Produto 02', 'preco': 20.00},
    {'nome': 'Produto 03', 'preco': 30.00},
    {'nome': 'Produto 04', 'preco': 40.00},
    {'nome': 'Produto 05', 'preco': 50.00}
]
def func_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']


total = reduce(
    func_reduce, 
    produtos,
    0
) 

print(f'Meu total é: {total}')
