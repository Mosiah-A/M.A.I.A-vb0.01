#importar sql
import pymysql

#conexaocom oservidor
con = pymysql.connect(
    host='localhost',
    user = 'root',
    password = '',
    database = 'TWD'
)

#execução de comandos

cursor = con.cursor()
cursor.execute("CREATE TABLE comhilltop (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255), arma VARCHAR (255))")
