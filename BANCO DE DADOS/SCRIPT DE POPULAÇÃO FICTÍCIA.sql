INSERT INTO Livro (titulo, autor, ano_publicacao, status) VALUES
('Dom Casmurro', 'Machado de Assis', 1899, 'disponível'),
('Memórias Póstumas de Brás Cubas', 'Machado de Assis', 1881, 'disponível'),
('Grande Sertão: Veredas', 'João Guimarães Rosa', 1956, 'emprestado'),
('A Moreninha', 'Joaquim Manuel de Macedo', 1844, 'disponível'),
('O Alquimista', 'Paulo Coelho', 1988, 'emprestado'),
('Vidas Secas', 'Graciliano Ramos', 1938, 'disponível'),
('O Guarani', 'José de Alencar', 1857, 'emprestado'),
('Capitães da Areia', 'Jorge Amado', 1937, 'disponível'),
('Iracema', 'José de Alencar', 1865, 'disponível'),
('O Cortiço', 'Aluísio Azevedo', 1890, 'disponível'),
('1984', 'George Orwell', 1949, 'disponível'),
('A Revolução dos Bichos', 'George Orwell', 1945, 'disponível'),
('Crime e Castigo', 'Fiódor Dostoiévski', 1866, 'emprestado'),
('O Processo', 'Franz Kafka', 1925, 'disponível'),
('Os Miseráveis', 'Victor Hugo', 1862, 'disponível'),
('Guerra e Paz', 'Liev Tolstói', 1869, 'disponível'),
('Cem Anos de Solidão', 'Gabriel García Márquez', 1967, 'disponível'),
('O Amor nos Tempos do Cólera', 'Gabriel García Márquez', 1985, 'disponível'),
('Ensaio sobre a Cegueira', 'José Saramago', 1995, 'emprestado'),
('Orgulho e Preconceito', 'Jane Austen', 1813, 'disponível');

INSERT INTO Cliente (nome, endereco, telefone) VALUES
('João da Silva', 'Rua A, 123', '11999990001'),
('Maria Oliveira', 'Rua B, 456', '11999990002'),
('Pedro Souza', 'Rua C, 789', '11999990003'),
('Ana Costa', 'Rua D, 101', '11999990004'),
('Carlos Lima', 'Rua E, 202', '11999990005'),
('Beatriz Gonçalves', 'Rua F, 303', '11999990006'),
('Rafael Almeida', 'Rua G, 404', '11999990007'),
('Fernanda Rodrigues', 'Rua H, 505', '11999990008'),
('Lucas Pereira', 'Rua I, 606', '11999990009'),
('Carla Santos', 'Rua J, 707', '11999990010');

INSERT INTO Emprestimo (livro_id, cliente_id, data_emprestimo) VALUES
(3, 1, '2024-09-15'), 
(5, 2, '2024-10-01'),  
(7, 3, '2024-10-05'),  
(13, 4, '2024-09-25'), 
(19, 5, '2024-10-10'); 
