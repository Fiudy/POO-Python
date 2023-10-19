class CadastroTime:
     def __init__ (self, nomeTime: str, cidade: str, mascote: str):
        self.nomeTime = nomeTime
        self.cidade = cidade
        self.mascote = mascote


class CadastroJogador:
    def __init__ (self, nomeJogador: str, nomeTime: str, numeroCamisa: str):
        self.nomeJogador = nomeJogador
        self.nomeTime = nomeTime
        self.numeroCamisa = numeroCamisa







class ComissaoTecnica:
    def __init__ (self, nome: str, nomeTime: str, esquemaTatico: str, ):
         self.nome = nome
         self.nometime = nomeTime
         self.esquematatico = ''
         self.preparar = ''


class Tecnicos(ComissaoTecnica):
     def __init__(self, nome: str, nomeTime: str, esquemaTatico: str):
        super().__init__(nome, nomeTime, esquemaTatico)

     def dar_coletiva (self):
         return 'O técnico está dando uma coletiva de imprensa'
         

class Auxiliares(Tecnicos):
    def __init__(self, nome: str, nomeTime: str, esquemaTatico: str=''):
        super().__init__(nome, nomeTime, esquemaTatico)

    def dar_coletiva (self):
         return 'O auxiliar está dando uma coletiva de imprensa'
         
       

class PreparadoresFisicos(ComissaoTecnica):

    def __init__(self, nome: str, nomeTime: str,preparar,esquemaTatico):
        super().__init__(nome, nomeTime, esquemaTatico)
        self.preparar = preparar

    def dar_coletiva (self):
         return "O preparador físico está dando uma coletiva de imprensa"