
from modelos.restaurante import Restaurante

restaurantes = [
    Restaurante('praça', 'Gourmet'),
    Restaurante('pizza express', 'Italiana')
]

restaurantes[1].alternar_status()
restaurantes[1].receber_avaliacao('Emy', 5)
restaurantes[1].receber_avaliacao('Erike', 5)
restaurantes[1].receber_avaliacao('João', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__  == '__main__':
    main()