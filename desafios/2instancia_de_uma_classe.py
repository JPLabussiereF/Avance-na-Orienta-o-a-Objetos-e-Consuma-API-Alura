# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem. Bora praticar então?
class Restaurante:
    nome = ''
    categoria = ''
    status = False

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza'
restaurante_pizza.categoria = 'Massas'

# Exercícios: 
# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(restaurante_praca.nome)

# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.status == True:
    print('Restaurante ativo')
else:
    print('Restaurante inativo')

# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria

# Altere o valor do atributo nome para 'Bistrô'.
restaurante_pizza.nome = 'Bistrô'

# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
print (f'Nome: {restaurante_pizza.nome} Categoria: {restaurante_pizza.categoria}')

# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
    print(f'A categoria do restaurante {restaurante_pizza.nome} é {restaurante_pizza.categoria}!')
else:
    print(f'A categoria do restaurante {restaurante_pizza.nome} não é Fast Food!')

# Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.status = True

# Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_praca.nome} Categoria: {restaurante_praca.categoria} Status: {restaurante_praca.status}')