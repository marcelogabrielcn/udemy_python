from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(Deposito de R${valor:.2f})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('----------------------------------------')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{class_name}, {attrs}'
    
class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(Saque {valor})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(Saque Negado {valor})')

class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float =0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(Saque {valor})')
            return self.saldo
    
        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(Saque Negado R${valor:.2f})')
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r}'
        return f'{class_name}, {attrs}'

if __name__ == '__main__':
    cp1 = ContaPoupanca(1111, 1029, 0)
    cp1.sacar(10)
    cp1.depositar(200)
    cp1.sacar(20)
    print('##')

    cp2 = ContaCorrente(2222, 3847, 0, 1000)
    cp2.sacar(10)
    cp2.depositar(2000)
    cp2.sacar(20)
    print('##')
