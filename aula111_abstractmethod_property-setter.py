from abc import ABC, abstractmethod


class AbstractFoo(ABC):  # *É uma classe abstrata, ou seja, não é para usar, é mais uma ideia do que fazer
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    @abstractmethod
    def name(self):
        return self._name


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print("Não sou útil nesse código")  # Esse parte é inútil porque o super apenas passa o código para classe pai


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

foo = Foo('Bar')
print(foo.name)
