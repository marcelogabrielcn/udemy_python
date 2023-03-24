# Ver aula 169, exercícios unir listas

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
uf = ['BA', 'SP', 'MG', 'RJ']

c = 0
nova_lista = []
for cidade in cidades:
    compiler = (cidades[c], uf[c])
    nova_lista.append(compiler)
    c += 1

print(nova_lista)


# Nesta aula vimos a função min e max, que retorna o mínimo ou máximo entre opções
# Outra forma de fazer é com Zip

print(list(zip(cidades, uf)))  # Beeeem mais fácil.

from itertools import zip_longest
print(list(zip_longest(cidades, uf)))  # Faz a mesma coisa, mas com a maior lista!
print(list(zip_longest(cidades, uf, fillvalue='Sem Cidade')))
