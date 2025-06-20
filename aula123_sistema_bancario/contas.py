import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abc.abstractclassmethod
    def sacar(self, valor):
        self.valor = valor
        self.detalhes(f'(Saque de R${valor:.2f})')

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(Deposito de R${valor:.2f})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('----------------------------------------')

class ContaPopanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(Saque {valor})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(Saque Negado {valor})')

if __name__ == '__main__':
    cp1 = ContaPopanca(3333, 1029, 0)
    cp1.sacar(1)
    cp1.depositar(1923)
    cp1.sacar(25)
