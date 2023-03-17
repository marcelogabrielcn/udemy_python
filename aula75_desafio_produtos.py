import copy

# *Ver aula 160 no curso da Udemy com proposta do desafio

produtos = [
    {'nome': 'Garrafa Tupperware', 'preco': 30.50},
    {'nome': 'Meditação Jovem 2023', 'preco': 22.80},
    {'nome': 'Cubo mágico 3x3', 'preco': 12.29},
    {'nome': 'Jogo de toalhas', 'preco': 74.90},
    {'nome': 'Relógio Kalenji', 'preco': 189.99},
]

produtos_com_aumento = []

for item in produtos:
    dict_temp = {
        'nome': item['nome'], 'preco': round((item['preco'] + (item['preco']/100) * 10), 2)
    }
    produtos_com_aumento.append(dict_temp)

    #produtos_com_aumento.append(item['nome'])
    #produtos_com_aumento.append(float(item['preco']) + (float(item['preco'])/100) * 10)
    #print(produtos_com_aumento)

#for produtos in produtos:
#   print(produtos)
print('Produtos originais')
print(*produtos, sep='\n')

#for produtos in produtos_com_aumento:
#    print(produtos)
print('\nProdutos com alteração de preço')
print(*produtos_com_aumento, sep='\n')

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos_com_aumento), key= lambda p: p['nome'], reverse=True)

print('\nProdutos ordenados por nome, em ordem decrescente')
print(*produtos_ordenados_por_nome, sep='\n')

produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos_com_aumento), key= lambda p: p['preco'])

print('\nProdutos ordenados por preço')
print(*produtos_ordenados_por_preco, sep='\n')
