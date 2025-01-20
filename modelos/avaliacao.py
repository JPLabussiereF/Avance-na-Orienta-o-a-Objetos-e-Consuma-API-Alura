class Avaliacao:
    """
    Classe que representa uma avaliação de um restaurante feita por um cliente.

    Atributos:
        cliente (str): Nome do cliente que realizou a avaliação.
        nota (float): Nota dada pelo cliente, variando de 0.0 a 5.0.

    Métodos:
        __init__(cliente, nota):
            Inicializa uma nova avaliação com os dados do cliente e a nota atribuída.
    """
    def __init__(self, cliente, nota):
        """
        Inicializa uma instância da classe Avaliacao.

        Args:
            cliente (str): Nome do cliente que fez a avaliação.
            nota (float): Nota atribuída pelo cliente, entre 0.0 e 5.0.
        """
        self._cliente = cliente,
        self._nota = nota
    
    @property
    def nota(self):
        """
        Obtém a nota atribuída na avaliação.

        Returns:
            float: A nota dada pelo cliente.
        """
        return self._nota
    @property
    def cliente(self):
        """
        Obtém o nome do cliente que fez a avaliação.

        Returns:
            str: O nome do cliente.
        """
        return self._cliente