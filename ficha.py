#importaçoes
import pymysql
from random import uniform

#interjeição
inter = ['Oi', 'Ola', 'Eai', 'Ei', '']

r = int(uniform(0, 100))
if (r < 48):
    s = inter[0]
elif (r < 52):
    s = inter[1]
elif (r < 84):
    s = inter[2]
elif (r < 92):
    s = inter[3]
elif (r > 100):
    s = inter[4]



#CODIGO PRINCIPAL
sexo = str(input('você é de qual sexo? [M/F] ')).strip().upper()
nome = str(input('Qual seu nome? ')).strip().title().split()
if(sexo == 'F'):
    sexo='Feminino'
    print('{}, é um prazer Sra. {}'.format(s, nome[0]))
else:
    sexo = 'Masculino'
    print('{} é um prazer Sr. {}'.format(s, nome[0]))
idade = int((input('Quantos anos você tem? ')))

#BANCO DE DADOS

#conexaocom oservidor
conexao = pymysql.connect(
    host='localhost',
    user = 'root',
    password = '',
    database = 'm.a.i.a'
)

#execução de comandos

cursor = conexao.cursor()

#instrução sql

com_sql = "INSERT INTO usuarios (nome, sexo, idade) VALUES (%s, %s, %s)"
valor = (nome, sexo, idade)
cursor.execute(com_sql, valor)

conexao.commit()

print(cursor.rowcount, "informação inserida")
