""""
Python não tem modificadores de acesso, como em outras linguagens,
Mas por convenção, tem algumas regrinhas que são usadas pelos devs

classe = Public
_classe = Protected
__classe = Private
"""

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'
        return self.__private

    def metodo_publico(self):
        return 'metodo publico'
    
    def _metodo_protected(self):
        return '_metodo protegido'

    def __metodo_private(self):
        return '__metodo privado'
    

f = Foo()
print(f.public)
print(f._protected)  # funciona, mas não deveria, por convenção, não se usa fora da classe
#print(f.__private)  # O Python bloqueia, não consigo acessar fora da classe.

print(f.metodo_publico())
print(f._metodo_protected())
#print(f.__metodo_private())

