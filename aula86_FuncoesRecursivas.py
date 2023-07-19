# Funções recursivas e recursividade 
# Trata-se de funções que pode chamar a própria função de volta
# TODA função recursiva precisa de uma base para ter um fim, caso contrário, a recursão fica infinita

def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        return fim
    
    print(inicio, fim)
    # Caso recursivo: contar até chegar até o final
    inicio += 1
    return recursiva(inicio, fim)  # Repare que a função retorna ela mesma e cria um loop


print(recursiva())
