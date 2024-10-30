import mysql.connector
from tabulate import tabulate

class BancoDeDados:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Admin123*',
            database='biblioteca'
        )
        self.cursor = self.conn.cursor()

    def inserir_livro(self, livro):
        sql = "INSERT INTO livro (titulo, autor, ano_publicacao, status) VALUES (%s, %s, %s, %s)"
        val = (livro.get_titulo(), livro.get_autor(), livro.get_ano_publicacao(), livro.get_status())
        self.cursor.execute(sql, val)
        self.conn.commit()
        print("Livro cadastrado com sucesso!")

    def inserir_cliente(self, cliente):
        sql = "INSERT INTO cliente (nome, endereco, telefone) VALUES (%s, %s, %s)"
        val = (cliente.get_nome(), cliente.get_endereco(), cliente.get_telefone())
        self.cursor.execute(sql, val)
        self.conn.commit()
        print("Cliente cadastrado com sucesso!")

    def registrar_emprestimo(self, titulo, nome_cliente):
        sql = "SELECT id FROM livro WHERE titulo = %s"
        self.cursor.execute(sql, (titulo,))
        livro = self.cursor.fetchone()

        if self.cursor._have_unread_result():
            self.cursor.fetchall()

        sql = "SELECT id FROM cliente WHERE nome = %s"
        self.cursor.execute(sql, (nome_cliente,))
        cliente = self.cursor.fetchone()

        if self.cursor._have_unread_result():
            self.cursor.fetchall()

        if livro and cliente:
            sql = "INSERT INTO emprestimo (livro_id, cliente_id, data_emprestimo) VALUES (%s, %s, NOW())"
            val = (livro[0], cliente[0])
            self.cursor.execute(sql, val)
            self.conn.commit()

            sql = "UPDATE livro SET status = 'emprestado' WHERE id = %s"
            self.cursor.execute(sql, (livro[0],))
            self.conn.commit()

            print("Empréstimo registrado com sucesso!")
        else:
            print("Livro ou cliente não encontrado.")

    def consultar_livros(self):
        self.cursor.execute("SELECT * FROM livro")
        livros = self.cursor.fetchall()
        colunas = ["ID", "Título", "Autor", "Ano de Publicação", "Status"]
        print(tabulate(livros, headers=colunas, tablefmt="grid"))

    def consultar_clientes(self):
        self.cursor.execute("SELECT * FROM cliente")
        clientes = self.cursor.fetchall()
        colunas = ["ID", "Nome", "Endereço", "Telefone"]
        print(tabulate(clientes, headers=colunas, tablefmt="grid"))

    def consultar_emprestimos(self):
        self.cursor.execute("""
            SELECT e.data_emprestimo, l.titulo, c.nome 
            FROM emprestimo e 
            JOIN livro l ON e.livro_id = l.id 
            JOIN cliente c ON e.cliente_id = c.id
        """)
        emprestimos = self.cursor.fetchall()
        colunas = ["Data de Empréstimo", "Livro", "Cliente"]
        print(tabulate(emprestimos, headers=colunas, tablefmt="grid"))

    def __del__(self):
        self.cursor.close()
        self.conn.close()