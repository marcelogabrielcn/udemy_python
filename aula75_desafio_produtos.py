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
        'nome': item['nome'], 'preco': (item['preco'] + (item['preco']/100) * 10)
    }
    produtos_com_aumento.append(dict_temp)
    print(produtos_com_aumento)
    #produtos_com_aumento.append(item['nome'])
    #produtos_com_aumento.append(float(item['preco']) + (float(item['preco'])/100) * 10)
    #print(produtos_com_aumento)
