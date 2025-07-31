import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.idade!r}'
        return f'{class_name}, {attrs}'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None
    

if __name__ == '__main__':
    c1 = Cliente('Gabriel', 26)
    c1.conta = contas.ContaCorrente(1234, 2345, 0, 100)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Lari', 22)
    c2.conta = contas.ContaCorrente(5678, 8393, 200, 1000)
    print(c2)
    print(c2.conta)
