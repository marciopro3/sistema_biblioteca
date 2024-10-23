class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} - {self.endereco} - {self.telefone}"