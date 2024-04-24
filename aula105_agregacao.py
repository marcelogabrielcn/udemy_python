class Carrinho:
    def __init__(self):
        self._produtos = []
    
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
    
    def listar_produtos(self):
        print()
        for p in self._produtos:
            print(p.nome, p.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho1 = Carrinho()
prod1, prod2 = Produto('Garrafa', 19.90), Produto('iPhone 13', 3900.00)
carrinho1.inserir_produtos(prod1, prod2)
carrinho1.listar_produtos()
print(carrinho1.total())