def soma(a, b):
    return a + b  # Função termina aqui, não é possível executar nada após o return


def multiplicador(a, b):
    if a % b == 0:
        return f'{a} é divisível por {b}'
    
    return f'{a} não é divisível por {b}'


atividade = soma(8, 9)
print(atividade)

divisor1 = multiplicador(8, 2)
divisor2 = multiplicador(9, 3)
divisor3 = multiplicador(18, 3)
divisor4 = multiplicador(8924, 3)
print(divisor1)
print(divisor2)
print(divisor3)
print(divisor4)
