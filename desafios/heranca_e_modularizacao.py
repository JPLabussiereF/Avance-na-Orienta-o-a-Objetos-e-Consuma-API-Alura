# A herança é um conceito fundamental na programação orientada a objetos (OO) e desempenha um papel crucial no desenvolvimento de software. A importância da herança está relacionada à capacidade de criar novas classes reutilizando ou estendendo o comportamento de classes existentes.

# Com base no que vimos nessa aula sobre herança, crie uma classe Banco com dois atributos: nome e endereco. Em seguida, derive uma classe chamada Agencia que herda os atributos da classe Banco e inclua um atributo adicional chamado numero. Ambas as classes devem ter apenas o construtor.

class Banco:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        
    def __str__(self):
        return f'{self.nome} - {self.endereco}'

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero = numero
    
    def __str__(self):
        return f'{self.nome} - {self.endereco} - {self.numero}'