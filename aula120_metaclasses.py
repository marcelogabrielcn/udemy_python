# Por herança, acima de qualquer classe, tenho a class OBJECT

class Foo:
    ...


f = Foo()
print(isinstance(f, Foo))
print()
print(type(f))
print(type(Foo))
