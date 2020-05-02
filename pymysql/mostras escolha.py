import pymysql

#configurando o banco de dados
conexao = pymysql.connect(
    host = 'localhost',
    user='root',
    password='',
    database='TWD'
)

cursor = conexao.cursor()
# cursor.execute('SELECT *  FROM comalexandria')
#cursor.execute('SELECT arma  FROM comalexandria')
cursor.execute("SELECT *  FROM comalexandria WHERE arma = 'Besta'")


resultado = cursor.fetchall() #busca por toda a tabela (varredura)

for x in resultado:
    print(x)