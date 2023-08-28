# Como salvar dados python com json

import json


pessoa = {
    'nome': 'Marcelo Gabriel',
    'sobrenome': 'Sousa',
    'enderecos': [
         {'rua': 'primeiro endereço', 'numero': 1234},
         {'rua': 'segundo endereço', 'numero': 4321}
    ],
    'altura': 1.83,
    'numeros_preferidos': (3, 7, 9),
    'dev': False,
    'qualquer_coisa': None
}

with open('aula91.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo)


# Desta forma, meus dados estão salvos em um arquivo json, de forma que posso importa-lo em outro lugar se precisar, desta forma: 

with open('aula91.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)

