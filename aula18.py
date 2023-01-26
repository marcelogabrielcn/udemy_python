"""
Interpolação básica de strings

s - string
d/i - int
f - float
x/X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Gabriel'
preco = 12790.1235623

var = '%s, o preço é R$%.2f' %(nome, preco)

print(var)

print('O hexadecimal de %d é igual a %04X' %(1122235, 1122235))
