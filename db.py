#importar sql
import pymysql

#conexaocom oservidor
con = pymysql.connect(
    host='localhost',
    user = 'root',
    password = '',
    database = 'M.A.I.A'
)

#execução de comandos

cursor = con.cursor()
cursor.execute("CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255), sexo VARCHAR (255), idade INT)")
