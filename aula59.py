s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9, 0}

s3 = s1 | s2  # União dos dois sets
s4 = s1 & s2  # Intersecção (Itens presentes nos dois)
s5 = s2 - s1  # Diferença entre o da esqueda para direita (itens presentes só na esquerda)
s6 = s2 ^ s1  # Diferença simétrica (Itens que não estão em ambos)

print(s3)
print(s4)
print(s5)
print(s6)
