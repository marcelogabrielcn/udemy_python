listinha = []

listinha.append(10)  # Adiciona elementos ao FINAL da lista
listinha.append(20)
listinha.append(30)
listinha.append(40)
listinha.append(50)
print(listinha)

del listinha[4]  # Deleta o item na posição especificada
print(listinha)


listinha.pop()  # Remove o ÚLTIMO item da lista e retorna cada vez que usar
ultimo_valor = listinha.pop()  # Agora o último valor ficará salvo nesta variável
print(listinha)
print(ultimo_valor)

listinha.append(40)
listinha.append(50)
print(listinha)

listinha.insert(1, 100)  # Adiciona um item na posição que quiser
print(listinha)
listinha.insert(3, 200)
print(listinha)

#listinha.clear()  # Limpa a lista

