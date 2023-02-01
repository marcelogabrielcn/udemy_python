nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seja bem-vindo {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaço(s)!')
    else:
        print('Seu nome não contém espaço(s)!')
    print(f'Seu nome contém {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Oops, parece que você não preencheu todos os campos.')
