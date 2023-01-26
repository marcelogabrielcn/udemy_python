nome = input('Digite um nome completo: ')
encontrar = input('Digite o que deseja verificar se existe no nome: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'Ops, não existe {encontrar} em {nome}')
