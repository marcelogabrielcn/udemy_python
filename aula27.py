# Calculadora Python

calc = True

while calc:
    entrada = input('Pressione "Enter" para continuar ou "sair" para encerrar o programa: ').lower()
    if entrada != 'sair':
        num1 = input('Digite um número: ')
        int_num1 = int(num1)
        oper = input('Digite a operação (+, -, /, *) >> ')
        num2 = input('Digite outro número: ')
        int_num2 = int(num2)
        if oper == '+':
            print(f'A soma de {num1} + {num2} é igual a: {int_num1+int_num2}')
        elif oper == '-':
            print(f'A subtração de {num1} - {num2} é igual a: {int_num1-int_num2}')
        elif oper == '/':
            print(f'A divisão entre {num1} / {num2} é igual a: {int_num1/int_num2}')
        elif oper == '*':
            print(f'A multiplicação de {num1} * {num2} é igual a: {int_num1*int_num2}')
        else:
            print('Ops, não entendi a operação.')
    else: 
        calc = False

print('Fim do programa.')
