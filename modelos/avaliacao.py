class Avaliacao:
    def __init__(self, cliente: str, nota: int): 
        '''
        Essa função é responsavel por adicionar a nota de cada cliente
            
        Parametros:
            - cliente (str): O nome do cliente
            - nota (int): Nota do Restaurante com valor minimo de 0
        '''
        self._cliente = cliente
        self._nota = nota
    def __str__(self) -> str:
        '''Retorna a representação em string das notas.'''
        return f'{self._cliente} - {self._nota}'