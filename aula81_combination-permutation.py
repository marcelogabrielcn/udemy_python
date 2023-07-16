# Aula de combinações, permutações e produto - Itertools
'''
Combinação - Ordem não importa, iterável, tamanho do grupo
Permutação - Ordem importa
Produto - Ordem importa e repete valores únicos
'''
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = ['João', 'Luiz', 'Gabriel', 'Ana']
camisetas = [['preta', 'branca'], ['p', 'm', 'g'], ['masculino', 'feminino'], ['algodão', 'poliéster']]

print(list(combinations(pessoas, 2)))  # Trata-se de um iterável, ou seja, vai immprimir um objeto, tenho que dar next para ver
print(*list(combinations(pessoas, 2))) 
print(*list(combinations(pessoas, 2)), sep ='\n')
print()
# Inves de utilizar esse formato para printar toda hora, vamos criar uma função que faça isso sempre.
print('Combinations')
print_iter(combinations(pessoas, 2))
# Neste caso a ordem não importa, ou seja, Ana e Gabriel, é a mesma coisa de Gabriel e Ana

# Já na permutation, a ordem importa, ou seja são duas combinações diferetes
print('Permutations')
print_iter(permutations(pessoas, 2))

#Produto
print('Produto')
print_iter(product(*camisetas))  # Gera um carteriaso, vai fazer todas as combinações possíveis, quanto mais opções, mais produtos terá

