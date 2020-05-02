import pymysql

#configurando o banco de dados
conexao = pymysql.connect(
    host = 'localhost',
    user='root',
    password='',
    database='TWD'
)

cursor = conexao.cursor()
com_sql = 'SELECT *  FROM comalexandria ORDER BY nome DESC'

cursor.execute(com_sql)

resultado = cursor.fetchall()

for x in resultado:
    print(x)