# Exercício 01 - Número inteiro, par ou ímpar?
num = input('Digite um número inteiro: ')

if num.isdigit():
    num_int = int(num)
    if num_int % 2 == 0:
        print('Você digitou um número par.')
    else:
        print('Você digitou um número ímpar.')
else:
        print('Opa, este não é um número inteiro!')



# Exercício 02 - Que horas são?
hora = input('Digite as horas em número inteiro (ex:14): ')
hora_int = int(hora)
if hora_int >= 0 and hora_int <= 12:
    print('Bom dia!')
elif hora_int >= 13 and hora_int <= 18:
    print('Boa tarde!')
elif hora_int >= 19 and hora_int <= 23:
    print('Boa noite!')
else:
    print('Ops, não entendi...')


# Exercício 03 - Nome curto?
nome = input('Digite seu nome: ')
if len(nome) <= 4:
    print('Seu nome é curto.')
elif len(nome) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande!')
