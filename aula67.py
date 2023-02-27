def generator(n):
    yield 1  # Pausar
    print('Continuando...1')
    yield 2  # Pausar
    print('Continuando...2')
    

gen = generator(0)
print(gen)
print(next(gen))
print(next(gen))

print('Acabou')
