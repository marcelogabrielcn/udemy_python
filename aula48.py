def soma(*args):  # Independente da quantidade de argumentos, ele aceita e cria uma tupla!
    total = 0
    for num in args:  # Existe a função sum() mas aqui foi só exemplo
        total += num
    return total


soma_par = soma(2, 4, 6, 8, 10)
print(soma_par)

soma_par2 = soma(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
print(soma_par2)
