import json

caminho_arquivo = 'aula97.json'


class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Gabriel', 25)
p2 = Pessoa('Ana', 22)
p3 = Pessoa('Julia', 21)

bd = [vars(p1), p2.__dict__, vars(p3)]  # vars vai pegar o dict desta variavel.


def fazer_dump():
    print('Fazendo o DUMP')
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
