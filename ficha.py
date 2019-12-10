sexo = str(input('você é de qual sexo? [M/F] ')).strip().upper()
user = str(input('Qual seu nome? ')).strip().title().split()
if(sexo == 'F'):
    print('{}, é um prazer Sra. {}'.format(s, user[0]))
else:
    print('{} é um prazer Sr. {}'.format(s, user[0]))
idade = int((input('Quantos anos você tem? ')))