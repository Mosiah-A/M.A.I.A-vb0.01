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

#comandos de execuçao de instrução

#com_sql = "UPDATE comalexandria SET ARMA = 'AR-15 ' "
#com_sql = "DELETE FROM comalexandria WHERE ARMA = 'Pistola' "
com_sql = "DROP TABLE comcomWolf"

cursor.execute(com_sql)
