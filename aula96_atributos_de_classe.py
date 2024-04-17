class Pessoa:
    atributo = 'valor'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return 2024 - self.idade
    
p1 = Pessoa('Gabriel', 24)
p2 = Pessoa('Daniel', 17)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

