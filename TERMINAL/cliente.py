class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_telefone(self):
        return self.__telefone