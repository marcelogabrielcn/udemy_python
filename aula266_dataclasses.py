from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade:int
    
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'



if __name__ == '__main__':
    
    p1 = Pessoa('Gabriel', 'Ferreira', 25)
    print(p1.nome_completo())