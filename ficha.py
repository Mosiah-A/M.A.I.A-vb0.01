#importaçoes

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
print('\033[31m ATENÇÃO ATIVE O SERVIDOR LOCAL WAMPP\033[m')

r=1
while r != 0:
    print('''Qual sua escolha:
    [1] Novo Usuario
    [2] Login Admin
    [0] Sair''')
    r = int(input())

#Novo Usuario

    if r == 1:
        sexo = str(input('você é de qual sexo? [M/F] ')).strip().upper()
        nome = str(input('Qual seu nome? ')).strip().title().split()
        if(sexo == 'F'):
            sexo='Feminino'
            print('{}, é um prazer Sra. {}'.format(s, nome[0]))
        else:
            sexo = 'Masculino'
            print('{} é um prazer Sr. {}'.format(s, nome[0]))
        anoDeNascimento = int((input('Qual ano você nasceu? ')))

        #BANCO DE DADOS1
        import pymysql

        #conexaocom oservidor
        conexao = pymysql.connect(
        host='localhost',
        user = 'root',
        password = '',
        database = 'm.a.i.a'
        )

        #execução de comandos

        cursor = conexao.cursor()

        #instrução sql1
        criarTabela = cursor.execute('''CREATE TABLE if not exists usuarios (
    id int(3) auto_increment,
    nome varchar(30) ,
    sexo varchar (1),
    nascimento int(4),
    primary key (id)
)default charset = utf8;''')
        #cursor.execute(criarTabela)
        #conexao.commit()

        com_sql = "INSERT INTO usuarios (nome, sexo, nascimento) VALUES (%s, %s, %s)"
        valor = (nome, sexo, anoDeNascimento)
        cursor.execute(com_sql, valor)

        conexao.commit()

        print(cursor.rowcount, "informação inserida")

#Usuario Admin

    elif r == 2:
        login = 'mosiah'
        senha = 'adms7777'
        login1 = input('Login: ')
        senha1 = input('Senha: ')
        if senha == senha1 and login == login1:
            print('Entrou.')
            print('{}, Mosiah.'.format(s))
            print('''O que deseja fazer? 
    [0] Sair''')
            r = int(input())
        else:
            print('Senha Invalida')

#sair

    elif r == 0:
        print('Saindo...')
    else:
        print('Erro, Tente novamente!')
    print('=-'*30)