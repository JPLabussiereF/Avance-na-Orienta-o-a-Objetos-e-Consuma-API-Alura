from modelos.cardapio.item_cardapio import ItemCardapio

class Bebidas(ItemCardapio):
    def __init__(self, nome, preco, descricao: str):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return f'{self.nome}({self.descricao}) - R$ {self.preco:.2f}\n'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
        