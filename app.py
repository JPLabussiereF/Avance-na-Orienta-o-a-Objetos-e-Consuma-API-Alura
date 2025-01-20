from modelos.restaurante import Restaurante

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

def main():
    """
    Função principal que lista os restaurantes cadastrados e exibe as informações do restaurante 'podrão do Labu'.

    Esta função chama o método de classe `listar_restaurantes` para exibir todos os restaurantes 
    registrados e, em seguida, imprime os detalhes do restaurante específico `restaurante_labu`.

    Returns:
        None
    """
    Restaurante.listar_restaurantes()
    print(f'\n{restaurante_labu}')

if __name__ == '__main__':
    """
    Ponto de entrada do script.

    Quando o script é executado diretamente, a função `main()` é chamada para listar os restaurantes 
    e exibir informações adicionais.
    """
    main()
