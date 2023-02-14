cpf = input('Digite seu CPF: ')
cpf_formatado = cpf.replace('.', "").replace('-', "")
print(cpf_formatado)

num_calc = 10
soma_9_prim_digit = 0

for n in cpf_formatado:
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


num_calc = 11
soma_10_prim_digit = 0

for n in cpf_formatado:
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

if cpf_formatado[0] * len(cpf_formatado) == cpf_formatado:
    print('CPF inválido!')
elif int(cpf_formatado[-2]) == d1 and int(cpf_formatado[-1]) == d2:
    print('CPF validado!')
else:
    print('Ops, parece que este CPF é inválido.')
