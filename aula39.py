frase = "Olha só, o que da pra fazer, com Split."

lista_palavras = frase.split()  # Separa em cada espaço em branco
print(lista_palavras)

separar_por_virgula = frase.split(',')  # Separa em cada caractere especificado
print(separar_por_virgula)

frase_com_espacos = "     Esta  frase   tinha   muitos     espaços     ."
palavras_frase = frase_com_espacos.split()
frase_sem_espacos = " "
for palavra in palavras_frase:
    #frase_sem_espacos.append(palavra.strip())
    frase_sem_espacos += palavra + " "

print(frase_sem_espacos.strip())
