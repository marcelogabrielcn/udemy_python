class Pessoa():
    def __init__(self, nome, sobrenome):
        ...


p1 = Pessoa()
p1.nome = 'Marcelo'
p1.sobrenome = 'Sousa'

p2 = Pessoa()
p2.nome = 'Gabriel'
p2.sobrenome = 'Ferreira'

p3 = Pessoa('Larissa', 'Marques')

print(p1.nome)
print(p2.nome)
print(p3.nome)
