"""
Formatação de strings

s - string
d - int
f - float
.<número de dígitos>f
x / X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex: 0>-100,.1f
Conversion flags - !r !s !a
"""

var = "abc"
print(f'{var: >10}')
print(f'{var: <10}')
print(f'{var: ^10}')
