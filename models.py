class Combustivel:
    def __init__(self, nome, preco_litro, estoque):
        self.nome = nome
        self.preco_litro = preco_litro
        self.estoque = estoque
    
    def vendas(self, litros):
        if litros <= 0:
            raise ValueError(f"Quantidade de {litros}L deve ser maior que 0")
        
        if litros > self.estoque:
            raise ValueError(f"Estoque de {litros}L insuficiente")
        
        self.estoque -= litros
        return litros * self.preco_litro
        