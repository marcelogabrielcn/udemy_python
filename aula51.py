# Exercice: Função que duplica, triplica e quadruplica algo 

def multiplicar(x):
    def duplicar(x):
        print(x * 2)
    def triplicar(x):
        print(x * 3)
    def quadruplicar(x):
        print(x * 4)
    duplicar(x)
    triplicar(x)
    quadruplicar(x)


multiplicar(10)

multiplicar(8)

multiplicar(19)
