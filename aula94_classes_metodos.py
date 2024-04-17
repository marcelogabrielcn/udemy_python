class Carro:
    def __init__(self, nome='Sem nome'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando!')


fusca = Carro('Fusca')
print(fusca.nome)

ferrari = Carro('Ferrari')
print(ferrari.nome)
ferrari.acelerar()

celtinha = Carro()
print(celtinha.nome)
