CREATE VIEW ViewEmprestimos AS
SELECT 
    e.id AS emprestimo_id,
    l.id AS livro_id,
    l.titulo AS titulo_livro,
    l.autor AS autor_livro,
    l.ano_publicacao,
    l.status AS status_livro,
    c.id AS cliente_id,
    c.nome AS nome_cliente,
    c.endereco AS endereco_cliente,
    c.telefone AS telefone_cliente,
    e.data_emprestimo
FROM 
    Emprestimo e
JOIN 
    Livro l ON e.livro_id = l.id
JOIN 
    Cliente c ON e.cliente_id = c.id;