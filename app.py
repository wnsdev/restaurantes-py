
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco_de_uva = Bebida('suco de uva', 4.90, '1L')
bebida_suco_de_uva.aplicar_desconto()

prato_feijoada = Prato('Feijoada', 19.90, 'feijõada bem caprichada e com bastante carne')
prato_feijoada.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco_de_uva)
restaurante_praca.adicionar_no_cardapio(prato_feijoada)

def main():
    restaurante_praca.exibir_carpio

if __name__  == '__main__':
    main()