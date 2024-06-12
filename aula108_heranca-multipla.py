# Quer dizer que uma classe pode herdar de mais de uma outra classe


class A():
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    def quem_sou(self):
        print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')

 
class D(B, C):
    ...

    def quea_sou(self):
        print('D')


dd = D()
dd.quea_sou()
print(D.mro())  # mro - Method Resolution Order (Mostra a ordem em que a hierarquia será consultada)

