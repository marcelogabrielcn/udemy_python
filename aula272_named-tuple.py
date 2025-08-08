from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'])
as_espada = Carta('A', '♠️')
print(as_espada)
print(as_espada.naipe)
print(as_espada[1])
print(as_espada.valor)
print(as_espada[0])
