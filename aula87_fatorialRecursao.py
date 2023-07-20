# Criando fatorial com funções recursivas 

def factorial(n):
    if n <= 1:
        return 1  # Caso base
    
    return n * factorial(n -1)


print(factorial(5))
