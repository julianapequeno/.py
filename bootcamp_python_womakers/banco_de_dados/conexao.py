# conectando com o banco de dados
import sqlite3

# minha conexao deste arquivo com o banco criado
conexao = sqlite3.connect('banco')
cursor = conexao.cursor()  # passando a conexao para uma nova variavel

# os camandos do banco vao aqui
# DDL - Data Definition Language

# cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100) );')

# cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
# cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
# cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

# cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100));')
# cursor.execute('DROP TABLE produtos')

# cursor.execute('INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(5,"Amanda","Canada","juju@gmail.ca", 0000000)')
# cursor.execute(
#   'INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(2,"Manuela","França","manuzinha@gmail.fra", 30923414)')
# cursor.execute(
#  'INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(3,"Nila","Inglaterra","nila@gmail.en", 438974)')
# cursor.execute(
# 'INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(4,"Salis","Inglaterra","salis@gmail.en", 3598327)')
# cursor.execute('DELETE FROM usuario where id=1')

# DML - Data Manipulation Language
# Unindo o python com o banco no print e select

# cursor.execute('SELECT * FROM usuario WHERE id>2')

# cursor.execute('UPDATE usuario SET endereco="Inglaterra" WHERE nome="Nila"')

# CLÁUSULAS

# ORDER BY & DESC
# dados = cursor.execute('SELECT * FROM usuario ORDER BY telefone, id DESC')  # primeiro ordenou pelo telefone e dps inverteu todos pela coluna do ID
# DESC -> Decrescente

# LIMIT E DISTINCT
# LIMIT -> Limita as info que vao ser retornadas
# dados = cursor.execute('SELECT * FROM usuario LIMIT 3')
# DISTINCT => Seleciona os valores UNICOS da coluna
# dados = cursor.execute('SELECT DISTINCT endereco FROM usuario ')

# GROUP BY & HAVING
# o HAVING é utiliza para filtrar resultados, exclusiva para o GRUPO BY. Após o processo de agregação feito pelo GRUPO BY
# o WHERE pode ser usado antes do processo de agregação do GROUP BY
# Se lembre de seguir a lógica de acordo com a ordem das cláusulas
# dados = cursor.execute('SELECT COUNT(nome),endereco FROM usuario WHERE id>1 GROUP BY endereco')
# dados = cursor.execute('SELECT COUNT(nome),endereco, id FROM usuario WHERE id>1 GROUP BY endereco HAVING id>2')


# JOIN's
# cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100) );')
# cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(5,"Amanda","Canada","juju@gmail.ca")')
# cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(1,"João","Suíça","joao@gmail.su")')

# JOIN - INNER JOIN -> Pega todas as info das tabelas e relaciona as linhas com correspondencia em ambas as tabelas
dados = cursor.execute(
    'SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

# JOIN - lEFT JOIN
dados = cursor.execute(
    'SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome')

# JOIN - RIGHT JOIN
dados = cursor.execute(
    'SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.id = gerentes.id')

# JOIN - FULL JOIN -> Retorna as linhas que dao match
dados = cursor.execute(
    'SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')

# SUB-CONSULTAS / sub-queries / sub-selecties
dados = cursor.execute(
    'SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')
for usuario in dados:
    print(usuario)

conexao.commit()  # vao ser enviadas informações, é a EXECUÇÃO no BANCO, o envio
conexao.close()  # Fechar a conexao para nao dar conflito caso nao seja fechado anteriormente
