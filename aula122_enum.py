"""
Enum = Enumeração
É usado para fazer a numeração de um determinado número de coisas

"""
import enum

Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
print(Direcoes(1), Direcoes.ESQUERDA, Direcoes['ESQUERDA'])
print(Direcoes(1).name, Direcoes['ESQUERDA'].value)


def mover(direcao):
    #if direcao not in ('cima', 'baixo', 'direita', 'esquerda'):
    #    raise ValueError('Direção não encontrada.')

    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada.')
    print(f'Movendo peão para {direcao}')


#mover('cima')
#mover('baixo')
#mover('esquerda')
#mover('direita')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)