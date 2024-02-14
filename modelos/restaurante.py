from modelos.avaliacao import Avaliacao
class Restaurante:
    '''Representa um restaurante e suas caracteristicas.'''
    restaurantes = []
    def __init__(self, nome: str, categoria: str):
        '''
        Inicia uma instancia de Restaurante.
        
        Parâmetros:
            - nome (str): o nome do restaurante.
            - categoria (str): a categoria do restaurante.
        '''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self): 
        '''Retorna a representação em string do restaurante.'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Exibi uma lista formatada de todos os restaurantes.'''
        heading = f'{"Nome do Restaurante".ljust(27)} {"Categoria".ljust(25)} {"Avaliação".ljust(25)} {"Status"}'
        print('▁' * heading.__len__())
        print(heading)
        print('▔' * heading.__len__())
        for restaurante in cls.restaurantes:
            print(f'▸ {restaurante._nome.ljust(25)} {restaurante._categoria.ljust(25)} {str(restaurante.media_avaliacoes).ljust(25)} {restaurante.ativo}')

    @property
    def ativo(self):
        '''Retorna um simbolo indicando o status do restaurante.'''
        return '🔹' if self._ativo else '🔸'
    
    def alternar_status(self):
        '''Alterna o status do restaurante.'''
        self._ativo = not  self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        '''
        Registra a avaliação do restaurante.
        
        parâmetros:
            - cliente  (str): o nome do cliente que fez a avaliação
            - nota (int): nota do resturante entre 0 e 5
        '''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property  
    def media_avaliacoes(self):
        '''Calcula a média das avaliações dos restaurantes.'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media