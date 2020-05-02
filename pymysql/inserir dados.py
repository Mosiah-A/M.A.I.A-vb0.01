#importar sql
import pymysql

#conexaocom oservidor
conexao = pymysql.connect(
    host='localhost',
    user = 'root',
    password = '',
    database = 'TWD'
)

#execução de comandos

cursor = conexao.cursor()

#instrução sql

com_sql = "INSERT INTO comalexandria (nome, arma) VALUES (%s, %s)"
valor = [
    ('Gleen','Pistola'),
    ('Deryl', 'Besta'),
    ('Carol', 'Metralhadora'),

]
cursor.executemany(com_sql, valor)

conexao.commit()

print(cursor.rowcount, "inserida")
