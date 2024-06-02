"""
Exercício com classes
1. Crie uma classe Carro (Nome)
2. Crie uma classe Motor (Nome)
3. Crie uma classe Fabricante (Nome)
4. Faça uma ligação entre Carro e Motor
Obs. Um motor pode ser de vários carros
5. Faça uma ligação entre Carro e Fabricante
Obs. Um Fabricante pode ter vários carros
Exiba o nome do Carro, motor e Fabricante na tela
"""

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None


    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, tipo):
        self._motor = tipo

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome

    
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
    

discovery = Carro('Discovery')
land_rover = Fabricante('Land Rover')
motor_3_0 = Motor('m3.0')
discovery.fabricante = land_rover
discovery.motor = motor_3_0

print(f'Nome: {discovery.nome}, Fabricante: {discovery.fabricante.nome}, Motor: {discovery.motor.nome}')
