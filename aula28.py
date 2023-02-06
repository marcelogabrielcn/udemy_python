frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Mauris ut velit cursus, malesuada tortor ut, posuere mi. \
Duis eleifend consequat eleifend. \
Etiam venenatis eros vitae magna interdum volutpat. \
Suspendisse potenti.'.lower()

i = 0
letra_q_mais_apareceu = ''
qtd_letra_q_mais_apareceu = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    if frase.count(letra_atual) > qtd_letra_q_mais_apareceu:
        qtd_letra_q_mais_apareceu = frase.count(letra_atual)
        letra_q_mais_apareceu = letra_atual

    # print(frase[i], frase.count(letra_atual))
    i += 1
print(f'A letra que mais apareceu foi "{letra_q_mais_apareceu}", aparecendo {qtd_letra_q_mais_apareceu}x ')

print('Fim do programa.')
