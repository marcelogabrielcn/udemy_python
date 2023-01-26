entrada = input('Olá, você deseja sacar ou depositar? ')

if entrada == "sacar":
    print('Você vai sacar um valor...')
elif entrada == "depositar":
    print('Você vai depositar um valor...')
else:
    print('Oops, você não digitou nenhuma das opções acima. Até logo.')

print('Fim do bloco.')
