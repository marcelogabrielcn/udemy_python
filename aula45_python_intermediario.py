# A partir daqui começamos no módulo "intermediário em Python

def imprimir(a, b, c='padrão'):
    print(f'Este é o primeiro argumento passado: {a}')
    print(f'Este é o segundo argumento passado: {b}')
    print(f'Este é o terceiro argumento passado: {c}')


palavra_1 = 'Qualquer coisa'
palavra_2 = 'Teste 2'
palavra_3 = 'Terceirão'

imprimir(palavra_1, palavra_2, palavra_3)

imprimir('Teste', 'Imprime aqui também', 58917.15)

imprimir('Só terão 2 argumentos', 9125)  # Se não for passado o terceiro arg, ele usa o valor padrão
