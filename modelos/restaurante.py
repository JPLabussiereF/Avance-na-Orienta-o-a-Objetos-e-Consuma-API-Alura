from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() # Método title() deixa a primeira letra de cada palavra maiúscula
        self._categoria = categoria.upper() # Método upper() deixa todas as letras maiúsculas
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    @property
    def nome(self):
        """
        Getter para o nome do restaurante.

        Returns:
            str: Nome do restaurante.
        """
        return self._nome
    def categoria(self):
        """
        Getter para a categoria do restaurante.

        Returns:
            str: Categoria do restaurante.
        """
        return self._categoria

    def __str__(self):
        """
        Retorna uma representação em string do restaurante.

        Returns:
            str: Representação em string do restaurante.
        """
        return f'Nome: {self._nome} | Categoria: {self._categoria} | Status: {self.status} | Avaliação: {self.media_avaliacoes}'
    
    @classmethod
    def listar_restaurantes(cls):
        """
        Lista todos os restaurantes cadastrados.

        """
        print(f'\n| {'Nome:':<30} | {'Categoria:':<30} | {'Status:':<30} | {'Avaliação:':<30} |')
        for restaurante in cls.restaurantes:
            print(f'| {restaurante._nome:<30} | {restaurante._categoria:<30} | {restaurante.status:<30} | {restaurante.media_avaliacoes:<30} |') 

    @property
    def status(self):
        """
        Retorna o status do restaurante (Aberto ou Fechado).

        Returns:
            str: Status do restaurante.
        """
        return 'Aberto' if self._status else 'Fechado'

    def alternar_status(self):
        """
        Alterna o status do restaurante entre Aberto e Fechado.
        """
        self._status = not self._status
    
    def receber_avaliacao(self, cliente, nota):
        """
        Recebe uma avaliação de um cliente e a armazena na lista de avaliações do restaurante.

        Args:
            cliente (str): Nome do cliente que fez a avaliação.
            nota (float): Nota da avaliação (de 0.0 a 5.0).

        Raises:
            ValueError: Se a nota não estiver dentro do intervalo de 0.0 a 5.0.
        """
        if nota < 0.0 or nota > 5.0:
            raise ValueError("A nota deve ser um valor entre 0.0 e 5.0!")
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """
        Calcula a média das avaliações recebidas pelo restaurante.

        Returns:
            str: Representação da média das avaliações (emojis de estrela + valor médio).
        """
        if not self._avaliacao:
            return 'Restaurante sem Avaliações'
        soma_das_notas = sum(avaliacao.nota for avaliacao in self._avaliacao)
        quantidade_de_avaliacoes = len(self._avaliacao)
        media_das_notas = round(soma_das_notas / quantidade_de_avaliacoes, 1)
        return f'{'★' * int(media_das_notas)} {media_das_notas}'

    def adicionar_item_no_cardapio(self,item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    # def adicionar_bebida_no_cardapio(self, bebida):
    #     self._cardapio.append(bebida)

    # def adicionar_prato_no_cardapio(self, prato):
    #     self._cardapio.append(prato)