import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


# cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# alunos = cursor.execute('SELECT * FROM alunos WHERE curso="BTI" ORDER BY nome')

# Q4 - alunos = cursor.execute('SELECT COUNT(nome) FROM alunos')

# Q5 - cursor.execute('UPDATE alunos SET idade=20 WHERE nome="Matheus"')
#  cursor.execute('DELETE FROM alunos WHERE id=5')

# cursor.execute('CREATE TABLE compras (id INT, cliente_id INT, produto VARCHAR(100), valor FLOAT);')
# cursor.execute(
#   'INSERT INTO clientes(id,nome,idade,saldo) VALUES(1,"Florinda",28,100.00)')

# cursor.execute('UPDATE clientes SET saldo=200.00 WHERE nome="Florinda"')
# cursor.execute('DELETE FROM clientes WHERE id=1')

# alunos = cursor.execute("INSERT INTO compras(id,cliente_id,produto,valor) VALUES(001,2,'Valorant',120.00)")
# alunos = cursor.execute('SELECT * FROM clientes WHERE saldo>1000.00 ')
alunos = cursor.execute(
    'SELECT nome,produto,valor FROM clientes LEFT JOIN compras ON clientes.id=compras.cliente_id')

for aluno in alunos:
    print(aluno)

conexao.commit()
conexao.close()
