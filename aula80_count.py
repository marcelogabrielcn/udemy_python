from itertools import count

c1 = count(0, 8)  # Count é infinito, CUIDADO!
r1 = range(0, 100, 8)

print('\nPrint do Count')
for i in c1:
    if i >=100:
        break
    print(i)

print('\nPrint do Range')
for i in r1:
    print(i)
