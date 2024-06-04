class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def falar_nome_classe(self):
        print(self.nome, self.idade, self.__class__.__name__)  # Vai pegar o nome da classe
    
    def falar_o_que_sou(self):
        print('Eu sou uma pessoa!')


class Aluno(Pessoa):
    def falar_o_que_sou(self):
        print('Eu sou um aluno!')


pessoa001 = Pessoa('Jorge', 'Silva', 34)
pessoa001.falar_nome_classe()
pessoa001.falar_o_que_sou()
aluno001 = Aluno('Gabriel', 'Ferreira', 25)
aluno001.falar_nome_classe()
aluno001.falar_o_que_sou()

