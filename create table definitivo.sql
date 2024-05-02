--Tabela com as informações dos usuários
CREATE SEQUENCE user_info_user_id_seq as integer;
CREATE TABLE user_info(
user_id int primary key DEFAULT nextval('user_info_user_id_seq'::regclass),
nome varchar(100),
idade int,
salario float,
convenio varchar(30),
inicio_empresa date
)

--Tabela de pedido de empréstimo
CREATE SEQUENCE user_new_loan_user_id_seq as integer;
CREATE TABLE user_new_loan(
new_loan_id int primary key DEFAULT nextval('user_new_loan_user_id_seq'::regclass),
user_id int,
margem_loan float,
valor_emprestimo float,
parcelas int
FOREIGN KEY (user_id) REFERENCES user_infon(user_id)
);
SELECT setval('user_new_loan_user_id_seq', 1000, false);

--Tabela com os empréstimos aprovados
CREATE SEQUENCE user_loan_approved_loan_a_id_seq;
CREATE TABLE user_loan_approved(
new_a_id int primary key DEFAULT nextval('user_loan_approved_loan_a_id_seq'::regclass),
user_id int,
inicio_loan date,
fim_loan date,
devendo boolean
FOREIGN KEY (new_loan_id) REFERENCES user_new_loan(new_loan_id)
);
SELECT setval('user_loan_approved_loan_a_id_seq', 2000, false);

--Tabela com os empréstimos reprovados
CREATE SEQUENCE user_loan_desapproved_loan_d_id_seq;
CREATE TABLE user_loan_desapproved(
loan_d_id INT PRIMARY KEY DEFAULT nextval('user_loan_desapproved_loan_d_id_seq'::regclass),
user_id INT,
ultimo_pedido date,
FOREIGN KEY (user_id) REFERENCES user_new_loan(user_id)
);
SELECT setval('user_loan_desapproved_loan_d_id_seq', 3000, false);