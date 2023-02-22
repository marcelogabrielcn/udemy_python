letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Você encontrou!!!')
        break

    print(letras)


# Set pode ser usado para jogo de advinha por exemplo... Ele salva apenas um valor, sem repeti-lo
# E é mais leve e funcional do que checar se esta letra já está nas 'letras'
