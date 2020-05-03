import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='m.a.i.a'
)

cursor= con.cursor()
#cursor.execute('''CREATE TABLE if not exists test (
#    nome varchar(30)
#)default charset = utf8;''')

cursor.execute('''drop table test''')


