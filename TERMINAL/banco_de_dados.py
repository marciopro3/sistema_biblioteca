import mysql.connector

class BancoDeDados:
    def __init__(self, host, usuario, senha, banco):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Admin123*',
            database='biblioteca'
        )
        self.cursor = self.conexao.cursor()

    def cadastrar_cliente(self, nome, endereco, telefone):
        sql = "INSERT INTO cliente (nome, endereco, telefone) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, endereco, telefone))
        self.conexao.commit()

    def cadastrar_livro(self, titulo, autor, ano_publicacao):
        sql = "INSERT INTO livro (titulo, autor, ano_publicacao) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (titulo, autor, ano_publicacao))
        self.conexao.commit()

    def cadastrar_emprestimo(self, livro_id, cliente_id, data_emprestimo):
        sql = "INSERT INTO emprestimo (livro_id, cliente_id, data_emprestimo) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (livro_id, cliente_id, data_emprestimo))
        self.conexao.commit()

    def consultar_clientes(self):
        self.cursor.execute("SELECT * FROM cliente")
        return self.cursor.fetchall()

    def consultar_livros(self):
        self.cursor.execute("SELECT * FROM livro")
        return self.cursor.fetchall()

    def consultar_emprestimos(self):
        self.cursor.execute("SELECT * FROM emprestimo")
        return self.cursor.fetchall()

    def alterar_cliente(self, cliente_id, nome, endereco, telefone):
        sql = "UPDATE cliente SET nome = %s, endereco = %s, telefone = %s WHERE id = %s"
        self.cursor.execute(sql, (nome, endereco, telefone, cliente_id))
        self.conexao.commit()

    def alterar_livro(self, livro_id, titulo, autor, ano_publicacao):
        sql = "UPDATE livro SET titulo = %s, autor = %s, ano_publicacao = %s WHERE id = %s"
        self.cursor.execute(sql, (titulo, autor, ano_publicacao, livro_id))
        self.conexao.commit()

    def deletar_cliente(self, cliente_id):
        sql = "DELETE FROM cliente WHERE id = %s"
        self.cursor.execute(sql, (cliente_id,))
        self.conexao.commit()

    def deletar_livro(self, livro_id):
        sql = "DELETE FROM livro WHERE id = %s"
        self.cursor.execute(sql, (livro_id,))
        self.conexao.commit()

    def consultar_emprestimos_com_clientes(self):
        sql = """
        SELECT c.nome AS nome_cliente, l.titulo AS titulo_livro
        FROM emprestimo e
        INNER JOIN cliente c ON e.cliente_id = c.id
        INNER JOIN livro l ON e.livro_id = l.id;
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conexao.close()