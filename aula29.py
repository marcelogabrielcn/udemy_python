import os

# Jogo da advinha

palavra_secreta = 'desbravador'
letras_acertadas = ''
tentativas = 0

print('Bem-vindo ao jogo da advinha')
print(f'Tente adivinhar a palavra: ', '*' * len(palavra_secreta))

while True:
    palavra_formada = ''
    letra_palpite = input('Digite uma letra: ')
    if len(letra_palpite) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_palpite in palavra_secreta:
        letras_acertadas += letra_palpite

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(palavra_formada)

    tentativas += 1
    if palavra_secreta == palavra_formada:
        os.system('cls')
        print('VOCÊ GANHOU!!!')
        print(f'A palara é: {palavra_secreta}')
        print(f'Você usou {tentativas} tentativas.')
        break

print('Fim do programa.')
