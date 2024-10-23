# Sistema de Gerenciamento de Biblioteca

Este repositório contém a atividade avaliativa desenvolvida para a disciplina de **Programação Orientada a Objetos**, ministrada pelo professor **Nivaldo** no curso de **Análise e Desenvolvimento de Sistemas** da **UNIFEOB**.

## Descrição do Projeto

O projeto consiste no desenvolvimento de um sistema de gerenciamento de biblioteca, com as seguintes funcionalidades:

- **Cadastro de Usuários**: Registro e gerenciamento de informações dos usuários da biblioteca.
- **Cadastro de Livros**: Inserção e manutenção dos dados dos livros disponíveis.
- **Empréstimos**: Controle dos empréstimos realizados, incluindo a data de empréstimo e os dados associados ao usuário e ao livro.

Foi implementado um sistema de **CRUD (Create, Read)** para cada entidade, com interação no terminal, utilizando Python e MySQL.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Banco de Dados:** MySQL

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `src/`: Contém os arquivos de código-fonte do sistema.
- `docs/`: Documentação do projeto com instruções de uso.
- `tests/`: Testes para validar as funcionalidades de CRUD.
- `README.md`: Este documento.

## Instruções de Instalação

1. Instale o Python na versão 3.12.
2. Configure o MySQL e crie o banco de dados utilizando os scripts SQL fornecidos.
3. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
4. Navegue até a pasta do projeto e execute o código:
   ```bash
   cd nome-do-repositorio
   python src/main.py
   ```

## Funcionalidades do CRUD

- **Usuários**: Cadastro e listagem de usuários.
- **Livros**: Registro e visualização de livros no sistema.
- **Empréstimos**: Registro de novos empréstimos e consulta.

## Estrutura do Banco de Dados

O banco de dados foi implementado diretamente em MySQL e inclui tabelas para usuários, livros e empréstimos, com relacionamentos adequados para o gerenciamento dos dados.

## Contribuição

Para contribuir com o projeto, faça um fork do repositório, crie uma nova branch com as suas alterações e envie um pull request.
