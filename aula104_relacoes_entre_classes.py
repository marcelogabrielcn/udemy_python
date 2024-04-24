class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self._ferramenta = ferramenta



class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo...'
    

escritor1 = Escritor('Gabriel')
caneta1 = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Maquina de Escrever')
escritor1.ferramenta = caneta1

print(escritor1.ferramenta.escrever())

print(caneta1.escrever())
print(maquina_de_escrever.escrever())

escritor1.ferramenta = maquina_de_escrever
print(escritor1.ferramenta.escrever())

