# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem.

# Desafios:
# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBacnaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
# Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self): 
        return f'\n{self._titular} tem R${self._saldo} em sua conta bancária.'

# conta1 = ContaBacnaria('João', 1000)
# conta2 = ContaBacnaria('Maria', 2000)

# print(conta1, conta2)

# Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    @classmethod
    def ativar_conta(cls):
        cls._ativo = not cls._ativo
    

# Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

# Crie uma instância da classe e imprima o valor da propriedade titular.
conta1 = ContaBacnaria('João', 1000)
print(conta1._titular)
# Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__ (self, nome, idade, cpf, endereco, telefone):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._endereco = endereco
        self._telefone = telefone
    def __str__(self):
        return f'\nNome: {self._nome}\nIdade: {self._idade}\nCPF: {self._cpf}\nEndereço: {self._endereco}\nTelefone: {self._telefone}'

# cliente1 = ClienteBanco('João', 25, '123.456.789-00', 'Rua das Flores, 123', '11 1234-5678')
# cliente2 = ClienteBanco('Maria', 30, '987.654.321-00', 'Rua das Rosas, 321', '11 8765-4321')  
# cliente3 = ClienteBanco('José', 40, '456.789.123-00', 'Rua das Margaridas, 456', '11 4321-8765')
# Crie um método de classe para a conta ClienteBanco.
    @classmethod
    def conta(cls):
        return f'\n{cls._nome} tem R${cls._saldo} em sua conta bancária.'