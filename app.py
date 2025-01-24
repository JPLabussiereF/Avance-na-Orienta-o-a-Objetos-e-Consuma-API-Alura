import os
from modelos.restaurante import Restaurante
from modelos.cardapio.pratos import Pratos
from modelos.cardapio.bebidas import Bebidas

# Criando instâncias da classe Restaurante e adicionando avaliações
restaurante_labu = Restaurante('podrão do Labu', 'Podrões')
restaurante_labu.receber_avaliacao('João', 5)
restaurante_labu.receber_avaliacao('Maria', 4)
restaurante_labu.receber_avaliacao('José', 5)
restaurante_labu.alternar_status()
restaurante_candinho = Restaurante('pastelaria do Candinho', 'Pastéis')
restaurante_candinho.receber_avaliacao('Greg', 5)
restaurante_novais = Restaurante('restaurante do Novais', 'Comida Caseira')
restaurante_novais.receber_avaliacao('Ana', 3)

# Criando instâncias da classe pratos e bebidas
prato1 = Pratos('Podrão', 10.00, 'Podrão com carne, queijo, alface e tomate')
bebida1 = Bebidas('Suco de Laranja', 5.00, 'Suco de laranja natural 300ml')
bebida1.aplicar_desconto()
prato1.aplicar_desconto()
restaurante_labu.adicionar_no_cardapio(prato1)
restaurante_labu.adicionar_no_cardapio(bebida1)

def main():
    os.system('cls')
    # Restaurante.listar_restaurantes()
    # print(f'\n{restaurante_labu}')
    restaurante_labu.listar_cardapio

if __name__ == '__main__':
    """
    Ponto de entrada do script.

    Quando o script é executado diretamente, a função `main()` é chamada para listar os restaurantes 
    e exibir informações adicionais.
    """
    main()
