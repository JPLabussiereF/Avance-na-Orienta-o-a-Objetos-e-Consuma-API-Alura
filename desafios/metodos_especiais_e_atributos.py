from abc import ABC, abstractmethod
# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem.

# Exercícios: 

# Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
# No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    @abstractmethod
    def ligar(self):
        self._ligado = not self._ligado
# Crie uma nova classe chamada Carro que herda da classe Veiculo.

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def ligar(self):
        super().ligar()
        print('Carro ligado' if self._ligado else 'Carro desligado')
# No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.

# Em um arquivo chamado main.py, importe a classe Carro.
# main.py
# from veiculo import Carro

# No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
veiculo1 = Carro('Fiat', 'Uno', 'Vermelho')
veiculo2 = Carro('Fusca', 'Volkswagen', 'Azul')
veiculo3 = Carro('Chevrolet', 'Onix', 'Preto')