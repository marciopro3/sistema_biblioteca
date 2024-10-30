from tabulate import tabulate

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, status='disponível'):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__status = status

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_ano_publicacao(self):
        return self.__ano_publicacao

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status