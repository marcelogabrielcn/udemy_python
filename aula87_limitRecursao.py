# Funções recursivas e recursividade 
# Trata-se de funções que pode chamar a própria função de volta
# TODA função recursiva precisa de uma base para ter um fim, caso contrário, a recursão fica infinita
import sys
sys.setrecursionlimit(1004)  # Essa parte quebra o limite padrão do python e seta um novo limite estipulado...CUIDADO!!


def recursiva(inicio=0, fim=1002):
    if inicio >= fim:
        return fim
    
    print(inicio, fim)
    # Caso recursivo: contar até chegar até o final
    inicio += 1
    return recursiva(inicio, fim)  # Repare que a função retorna ela mesma e cria um loop


print(recursiva())
