# No Python, a criação de classes é uma parte essencial da programação orientada a objetos. Abaixo, temos um exemplo de uma classe chamada Musica que representa informações sobre uma música, como nome, artista e duração:
    # class Musica:
    #     nome = ''
    #     artista = ''
    #     duracao = int
# Agora é sua vez! Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python.

class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    def __str__(self):
        return f'Nome: {self.nome} Artista: {self.artista} Duração: {self.duracao}'

one_one_five = Musica('115', 'Elena Siegman', 228)
someone_beautiful = Musica('Destroy Someone Beautiful', 'Cristina Scabbia', 262)
fall_down = Musica('We All Fall Down', 'Kevin Sherwood', 183)
