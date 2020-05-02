# importando o bancode dados
import pymysql

#configurando o banco de dados
conexao = pymysql.connect(
    host = 'localhost',
    user='root',
    password='',
    database='TWD'
)

cursor = conexao.cursor()

cursor.execute("SHOW TABLES")

#apresentando informaçoes (ESTRUTURA DE REPETIÇÃO LOOP FOR)
for x in cursor:
    print(x)