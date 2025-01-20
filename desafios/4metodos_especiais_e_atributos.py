# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem.
# Exercícios:
# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    def __str__(self):
        return f'Modelo: {self.modelo} Cor: {self.cor} Ano: {self.ano}'
    
meu_carro = Carro('Fusca', 'Azul', 1970)

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome, categoria,  prato_principal, tempo_medio_de_preparo, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.prato_principal = prato_principal
        self.tempo_medio_de_preparo = tempo_medio_de_preparo
        self.ativo = ativo
    def __str__(self):
        return f'| Nome: {self.nome} | Categoria: {self.categoria} | Prato Principal: {self.prato_principal} | Tempo Médio de Preparo: {self.tempo_medio_de_preparo}'
    
primeiro_restaurante = Restaurante('Pizzaria', 'Fast Food', 'Pizza de Calabresa', 30, True)
print(primeiro_restaurante)

# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# class Restaurante:
#     def __init__(self, nome, categoria, ativo=False):
#         self.nome = nome
#         self.categoria = categoria
#         self.ativo = ativo
#     def __str__(self):
#         return f'| Nome: {self.nome} | Categoria: {self.categoria}'
# segundo_restaurante = Restaurante(nome='Churrascaria', categoria='Fast Food')
# print(segundo_restaurante)
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
    # def __str__(self):
    #     return f'| Nome: {self.nome} | Categoria: {self.categoria} | Prato Principal: {self.prato_principal} | Tempo Médio de Preparo: {self.tempo_medio_de_preparo}'
# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    def __init__(self, nome, idade, telefone, email):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
    def __str__(self):
        return f'\n| Nome: {self.nome} | Idade: {self.idade} | Telefone: {self.telefone} | Email: {self.email}'

cliente_1 = Cliente('João Pedro', 25, '+11 9 9999-9999', 'joao@gmail.com')
cliente_2 = Cliente('Maria Clara', 30, '+11 9 9999-9998', 'maria@gmail.com')
cliente_3 = Cliente('José Pinto', 35, '+11 9 9999-9997', 'jose@gmail.com')

print(cliente_1, cliente_2, cliente_3)

