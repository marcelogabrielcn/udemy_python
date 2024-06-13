class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        #print('parte do Property')
        return self._cor
    
    @cor.setter
    def cor(self, info):
        if info == 'Verde':
            raise ValueError('Não aceito essa cor.')
        #print('Parte do setter', info)
        self._cor = info

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, info):
        self._cor_tampa = info

def mostrar(caneta):
    return caneta.cor


caneta1 = Caneta('Azul')
print(caneta1.cor)
print(caneta1.cor_tampa)
caneta1.cor = 'Amarelo'  # Para configurar um atributo, usa-se o getter
caneta1.cor_tampa = 'Verde'
print(caneta1.cor)
print(caneta1.cor_tampa)

