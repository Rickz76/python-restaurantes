from modelos.avaliacao import Avaliacao

class Restaurante: # Define uma nova CLASSE chamada Restaurante
    restaurantes = [] # Serve como registro global: todo Restaurante criado é guardado aqui

    def __init__(self,nome,categoria):
        self._nome = nome.title() # Armazena o nome com a primeira letra de cada palavra maiúscula. _nome com underline indica "protegido" por convenção (não é privado de verdade, apenas sinaliza)

        self._categoria = categoria.upper() # .upper deixa tudo em caps look
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self) # Adiciona esse novo objeto dentro da lista.

    def __str__(self): # Define como o objeto se comporta quando alguém tenta imprimir ele diretamente
        return f'{self._nome} | {self._categoria} | {self.ativo}'
        
    @classmethod # Um "@algo" antes de uma função é um "decorador", ele muda o comportamento daquela função
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | {'Status'.ljust(25)}') # .ljust(25) deixa o texto ocupar 25 espaços, alinhando tudo à esquerda — é só pra deixar a tabela certinha no terminal
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas,1) # round garente que vai ter so uma (ou o numero que expecificar) casa decimal
        
        return media