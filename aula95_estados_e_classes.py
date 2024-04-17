class Camera: 
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"{self.nome} já está filmando.")
            return

        print(f"{self.nome} está filmando...")
        self.filmando = True

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()

print(c1.filmando)
print(c2.filmando)

