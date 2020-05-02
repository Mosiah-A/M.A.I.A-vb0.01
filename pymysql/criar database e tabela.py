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
# cursor.execute("CREATE TABLE comalexandria(nome VARCHAR(255),arma VARCHAR (255))")   # #CRIAR TABELA

comunit = str(input('Digite o nome do database: ')).strip()

cursor.execute("CREATE TABLE com{} (nome VARCHAR(255),arma VARCHAR (255))".format(comunit))


