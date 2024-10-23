import mysql.connector

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
        # Consultar o id do livro pelo título
        sql = "SELECT id FROM livro WHERE titulo = %s"
        self.cursor.execute(sql, (titulo,))
        livro = self.cursor.fetchone()

        # Certificar que o resultado foi consumido
        if self.cursor._have_unread_result():
            self.cursor.fetchall()

        # Consultar o id do cliente pelo nome
        sql = "SELECT id FROM cliente WHERE nome = %s"
        self.cursor.execute(sql, (nome_cliente,))
        cliente = self.cursor.fetchone()

        # Certificar que o resultado foi consumido
        if self.cursor._have_unread_result():
            self.cursor.fetchall()

        if livro and cliente:
            # Inserir o empréstimo na tabela emprestimo
            sql = "INSERT INTO emprestimo (livro_id, cliente_id, data_emprestimo) VALUES (%s, %s, NOW())"
            val = (livro[0], cliente[0])
            self.cursor.execute(sql, val)
            self.conn.commit()

            # Atualizar o status do livro para 'emprestado'
            sql = "UPDATE livro SET status = 'emprestado' WHERE id = %s"
            self.cursor.execute(sql, (livro[0],))
            self.conn.commit()

            print("Empréstimo registrado com sucesso!")
        else:
            print("Livro ou cliente não encontrado.")

    def consultar_livros(self):
        self.cursor.execute("SELECT * FROM livro")
        for livro in self.cursor.fetchall():
            print(livro)

    def consultar_clientes(self):
        self.cursor.execute("SELECT * FROM cliente")
        for cliente in self.cursor.fetchall():
            print(cliente)

    def consultar_emprestimos(self):
        self.cursor.execute("""
            SELECT e.data_emprestimo, l.titulo, c.nome 
            FROM emprestimo e 
            JOIN livro l ON e.livro_id = l.id 
            JOIN cliente c ON e.cliente_id = c.id
        """)
        for emprestimo in self.cursor.fetchall():
            print(emprestimo)

    def __del__(self):
        self.cursor.close()
        self.conn.close()