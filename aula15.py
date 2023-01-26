print('Olá, seja bem-vindo')
entrada = input('Digite "E" para entrar ou "S" para sair: ')
senha = input('Digite sua senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha == senha_permitida:
    print('Entrada bem sucedida')
else: 
    print('Oops, algo deu errado. Até logo...')
