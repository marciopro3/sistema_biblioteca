import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from banco_de_dados import BancoDeDados

class BibliotecaApp:
    def __init__(self, master):
        self.banco = BancoDeDados('localhost', 'root', 'Admin123*', 'biblioteca')

        master.title("Sistema de Biblioteca")
        master.geometry("400x400")

        # Criação do Notebook (abas)
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill='both', expand=True)

        # Abas
        self.abas_inserir = ttk.Frame(self.notebook)
        self.abas_visualizar = ttk.Frame(self.notebook)
        self.abas_alterar = ttk.Frame(self.notebook)
        self.abas_excluir = ttk.Frame(self.notebook)

        self.notebook.add(self.abas_inserir, text='Inserir')
        self.notebook.add(self.abas_visualizar, text='Visualizar')
        self.notebook.add(self.abas_alterar, text='Alterar')
        self.notebook.add(self.abas_excluir, text='Excluir')

        self.criar_aba_inserir()
        self.criar_aba_visualizar()
        self.criar_aba_alterar()
        self.criar_aba_excluir()

    def criar_aba_inserir(self):
        tk.Label(self.abas_inserir, text="Cadastrar Cliente").pack(pady=10)
        tk.Button(self.abas_inserir, text="Cliente", command=self.cadastrar_cliente).pack(pady=5)
        tk.Label(self.abas_inserir, text="Cadastrar Livro").pack(pady=10)
        tk.Button(self.abas_inserir, text="Livro", command=self.cadastrar_livro).pack(pady=5)
        tk.Label(self.abas_inserir, text="Cadastrar Empréstimo").pack(pady=10)
        tk.Button(self.abas_inserir, text="Empréstimo", command=self.cadastrar_emprestimo).pack(pady=5)

    def criar_aba_visualizar(self):
        tk.Label(self.abas_visualizar, text="Mostrar Clientes").pack(pady=10)
        tk.Button(self.abas_visualizar, text="Visualizar Clientes", command=self.mostrar_clientes).pack(pady=5)
        tk.Label(self.abas_visualizar, text="Mostrar Livros").pack(pady=10)
        tk.Button(self.abas_visualizar, text="Visualizar Livros", command=self.mostrar_livros).pack(pady=5)
        tk.Label(self.abas_visualizar, text="Mostrar Empréstimos").pack(pady=10)
        tk.Button(self.abas_visualizar, text="Visualizar Empréstimos", command=self.mostrar_emprestimos).pack(pady=5)
        tk.Button(self.abas_visualizar, text="Visualizar Empréstimos com Clientes", command=self.mostrar_emprestimos_com_clientes).pack(pady=5)

    def criar_aba_alterar(self):
        tk.Label(self.abas_alterar, text="Alterar Cliente").pack(pady=10)
        tk.Button(self.abas_alterar, text="Alterar Cliente", command=self.alterar_cliente).pack(pady=5)
        tk.Label(self.abas_alterar, text="Alterar Livro").pack(pady=10)
        tk.Button(self.abas_alterar, text="Alterar Livro", command=self.alterar_livro).pack(pady=5)

    def criar_aba_excluir(self):
        tk.Label(self.abas_excluir, text="Deletar Cliente").pack(pady=10)
        tk.Button(self.abas_excluir, text="Deletar Cliente", command=self.deletar_cliente).pack(pady=5)
        tk.Label(self.abas_excluir, text="Deletar Livro").pack(pady=10)
        tk.Button(self.abas_excluir, text="Deletar Livro", command=self.deletar_livro).pack(pady=5)

    def cadastrar_cliente(self):
        nome = simpledialog.askstring("Nome do Cliente", "Digite o nome do cliente:")
        endereco = simpledialog.askstring("Endereço do Cliente", "Digite o endereço do cliente:")
        telefone = simpledialog.askstring("Telefone do Cliente", "Digite o telefone do cliente:")
        self.banco.cadastrar_cliente(nome, endereco, telefone)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

    def mostrar_clientes(self):
        clientes = self.banco.consultar_clientes()
        self.mostrar_lista("Clientes", clientes)

    def alterar_cliente(self):
        cliente_id = simpledialog.askinteger("ID do Cliente", "Digite o ID do cliente que deseja alterar:")
        nome = simpledialog.askstring("Nome do Cliente", "Digite o novo nome do cliente:")
        endereco = simpledialog.askstring("Endereço do Cliente", "Digite o novo endereço do cliente:")
        telefone = simpledialog.askstring("Telefone do Cliente", "Digite o novo telefone do cliente:")
        self.banco.alterar_cliente(cliente_id, nome, endereco, telefone)
        messagebox.showinfo("Sucesso", "Cliente alterado com sucesso!")

    def deletar_cliente(self):
        cliente_id = simpledialog.askinteger("ID do Cliente", "Digite o ID do cliente que deseja deletar:")
        self.banco.deletar_cliente(cliente_id)
        messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")

    def cadastrar_livro(self):
        titulo = simpledialog.askstring("Título do Livro", "Digite o título do livro:")
        autor = simpledialog.askstring("Autor do Livro", "Digite o autor do livro:")
        ano_publicacao = simpledialog.askinteger("Ano de Publicação", "Digite o ano de publicação do livro:")
        self.banco.cadastrar_livro(titulo, autor, ano_publicacao)
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")

    def mostrar_livros(self):
        livros = self.banco.consultar_livros()
        self.mostrar_lista("Livros", livros)

    def alterar_livro(self):
        livro_id = simpledialog.askinteger("ID do Livro", "Digite o ID do livro que deseja alterar:")
        titulo = simpledialog.askstring("Título do Livro", "Digite o novo título do livro:")
        autor = simpledialog.askstring("Autor do Livro", "Digite o novo autor do livro:")
        ano_publicacao = simpledialog.askinteger("Ano de Publicação", "Digite o novo ano de publicação do livro:")
        self.banco.alterar_livro(livro_id, titulo, autor, ano_publicacao)
        messagebox.showinfo("Sucesso", "Livro alterado com sucesso!")

    def deletar_livro(self):
        livro_id = simpledialog.askinteger("ID do Livro", "Digite o ID do livro que deseja deletar:")
        self.banco.deletar_livro(livro_id)
        messagebox.showinfo("Sucesso", "Livro deletado com sucesso!")

    def cadastrar_emprestimo(self):
        livro_id = simpledialog.askinteger("ID do Livro", "Digite o ID do livro que deseja emprestar:")
        cliente_id = simpledialog.askinteger("ID do Cliente", "Digite o ID do cliente que está pegando emprestado:")
        data_emprestimo = simpledialog.askstring("Data do Empréstimo", "Digite a data do empréstimo (YYYY-MM-DD):")
        self.banco.cadastrar_emprestimo(livro_id, cliente_id, data_emprestimo)
        messagebox.showinfo("Sucesso", "Empréstimo cadastrado com sucesso!")

    def mostrar_emprestimos(self):
        emprestimos = self.banco.consultar_emprestimos()
        self.mostrar_lista("Empréstimos", emprestimos)

    def mostrar_emprestimos_com_clientes(self):
        emprestimos_com_clientes = self.banco.consultar_emprestimos_com_clientes()
        self.mostrar_lista("Empréstimos com Clientes", emprestimos_com_clientes)

    def mostrar_lista(self, titulo, dados):
        lista = tk.Toplevel()
        lista.title(titulo)
        for i, dado in enumerate(dados):
            tk.Label(lista, text=dado).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()