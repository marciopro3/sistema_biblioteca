from datetime import datetime
from tabulate import tabulate

class Emprestimo:
    def __init__(self, livro, cliente):
        self.__livro = livro
        self.__cliente = cliente
        self.__data_emprestimo = datetime.now()

    def get_livro(self):
        return self.__livro

    def get_cliente(self):
        return self.__cliente

    def get_data_emprestimo(self):
        return self.__data_emprestimo