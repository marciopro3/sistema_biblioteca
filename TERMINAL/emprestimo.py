class Emprestimo:
    def __init__(self, livro_id, cliente_id):
        self.livro_id = livro_id
        self.cliente_id = cliente_id

    def __str__(self):
        return f"Empréstimo do Livro ID: {self.livro_id} para Cliente ID: {self.cliente_id}"