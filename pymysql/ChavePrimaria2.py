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
cursor.execute("ALTER TABLE  comsalvadores ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
