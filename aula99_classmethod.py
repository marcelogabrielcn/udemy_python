'''
São métodos de classe + factories (fábricas)
São métodos onde "self" será "cls", ou seja, a própria classe em si.
Ao invés de receber a instancia, no self, ele recbe a própria classe
'''

class Pessoa:
    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("Hey, aqui é o método de classe.")

    @classmethod
    def criar_pessoa_50_anos(cls, nome):
        return cls(nome, 50)  # Esse cls, será o mesmo que passar Pessoa(nome, 50)
    

    @classmethod
    def criar_pessoa_sem_nome(cls, idade):
        return cls("Anônimo", idade)
    

p1 = Pessoa('João', 19)
p2 = Pessoa.criar_pessoa_50_anos("Maria")

p4 = Pessoa.criar_pessoa_sem_nome(23)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
#print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
