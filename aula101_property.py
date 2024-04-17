class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return(self.cor_tinta)
    
###############################################

caneta = Caneta('azul')
caneta2 = Caneta('vermelha')
print(caneta.cor_tinta)
print(caneta.cor_tinta)  # Aqui estou utilizando diretamente da classe, de forma que caso haja mudança, tem que alterar o code full

print(caneta2.cor)  # Aqui utilizo o propety, que se precisar mudar, altera somente la
print(caneta2.cor)
