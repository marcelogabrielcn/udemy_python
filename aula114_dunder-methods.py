class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        class_name1 = self.__class__.__name__
        class_name2 = type(self).__name__  # Mesma coisa da class_name1
        return f'{class_name2}(x={self.x}, y={self.y})' 


p1 = Ponto(1, 2)
p2 = Ponto(293, 421)
print(p1)
print(p2)
print()
print(repr(p2))
print(f'{p2!s}')
print(f'{p1!r}')

# O repr retorna para outros devs como a classe trata os objetos
