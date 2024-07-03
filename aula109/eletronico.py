from log import LogPrintMixin


class Eletronico:
    def __init__(self, nome, estado=False):
        self._nome = nome
        self._estado = estado

    def ligar(self):
        if not self._estado:
            self._estado = True

    def desligar(self):
        if self._estado == True:
            self._estado = False


class Smarthphone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()  # Passa a função para classe pai (Eletronico) e utiliza a função de la

    def desligar(self):
        super().desligar() 
