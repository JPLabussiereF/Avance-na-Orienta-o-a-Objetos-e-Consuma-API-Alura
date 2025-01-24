from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tamanho, tipo):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        self._descricao = descricao
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()} Tamanho: {self._tamanho} Descrição: {self._descricao}'
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.03