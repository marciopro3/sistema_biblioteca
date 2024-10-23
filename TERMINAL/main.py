from livro import Livro
from cliente import Cliente
from emprestimo import Emprestimo
from banco_de_dados import BancoDeDados


def menu():
    print("Sistema de Gerenciamento de Biblioteca")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Cliente")
    print("3. Registrar Empréstimo")
    print("4. Consultar Livros")
    print("5. Consultar Clientes")
    print("6. Consultar Empréstimos")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    banco = BancoDeDados()
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano_publicacao = input("Ano de publicação: ")
            livro = Livro(titulo, autor, ano_publicacao)
            banco.inserir_livro(livro)
        
        elif opcao == '2':
            nome = input("Nome do cliente: ")
            endereco = input("Endereço do cliente: ")
            telefone = input("Telefone do cliente: ")
            cliente = Cliente(nome, endereco, telefone)
            banco.inserir_cliente(cliente)
        
        elif opcao == '3':
            titulo = input("Título do livro para empréstimo: ")
            nome_cliente = input("Nome do cliente: ")
            banco.registrar_emprestimo(titulo, nome_cliente)
        
        elif opcao == '4':
            banco.consultar_livros()
        
        elif opcao == '5':
            banco.consultar_clientes()
        
        elif opcao == '6':
            banco.consultar_emprestimos()
        
        elif opcao == '0':
            print("Saindo do sistema.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()