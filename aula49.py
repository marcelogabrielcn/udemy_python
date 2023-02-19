# Desafio 01 - Def que multiplica todos os args

def multiplicar(*args):
    total_multiplicacao = 0
    for num in args:
        if total_multiplicacao == 0:
            total_multiplicacao += num
        else:
            total_multiplicacao *= num
    return total_multiplicacao


multiplicacaozinha = multiplicar(2, 2, 2, 2, 10)
multiplicacaozinha2 = multiplicar(2, 2, 2, 2, 10, 0)
multiplicacaozinha3 = multiplicar(1, 2, 3, 4, 5)
print(multiplicacaozinha)
print(multiplicacaozinha2)
print(multiplicacaozinha3)
