condicao = True
while condicao:
    nome = input('Digite o seu nome: ')
    print(f'Seja bem-vindo {nome}')

    if nome == 'sair':
        break
print('Fim do while')
