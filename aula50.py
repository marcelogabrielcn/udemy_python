# Desafio 02 - Def que retorna se num é par ou ímpar

def verifica_par_impar(x):
    if x % 2 == 0:
        return f'O número {x} é par!'
    return f'O número {x} é ímpar!'


eh_par = verifica_par_impar(8)
eh_par2 = verifica_par_impar(9)
eh_par3 = verifica_par_impar(823)
eh_par4 = verifica_par_impar(888)

print(eh_par)
print(eh_par2)
print(eh_par3)
print(eh_par4)
