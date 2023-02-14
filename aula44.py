import random


# Gerador de CPF
cpf = ''
primeiros_9_digitos = ''

for n in range(9):
    primeiros_9_digitos += str(random.randint(0, 9))

cpf += primeiros_9_digitos
print(primeiros_9_digitos)

num_calc = 10
soma_9_prim_digit = 0

for n in cpf:
    if num_calc > 1:
        mult_temp = int(n) * num_calc
        soma_9_prim_digit += mult_temp
        num_calc -= 1
        mult_temp = 0
    else: 
        break

check_d1 = soma_9_prim_digit * 10
check_d1 = check_d1 % 11
d1 = check_d1 if check_d1 <= 9 else 0
print(f'O primeiro dígito é {d1}')

cpf += str(d1)

num_calc = 11
soma_10_prim_digit = 0

for n in cpf:
    if num_calc > 1:
        mult_temp = int(n) * num_calc
        soma_10_prim_digit += mult_temp
        num_calc -= 1
        mult_temp = 0
    else:
        break

check_d2 = (soma_10_prim_digit * 10) % 11
d2 = 0 if check_d2 > 9 else check_d2

print(f'O segundo dígito é {d2}')
cpf += str(d2)

print(cpf)

