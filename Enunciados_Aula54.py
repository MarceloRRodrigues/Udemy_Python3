"""
EXERCÍCIO 1-->
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


"""
EXERCÍCIO 2-->
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
EXERCÍCIO 3-->
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

#EXERCICIO 1
numero = input('Digite um número inteiro: ')
try:
    numero_int = int(numero)
    if numero_int%2==0:
        print('\nÉ um número par')
    else: print('\nÉ um número impar')
except:
    print('\nNão é um número inteiro')

#EXERCICIO 2
hora = input('Que horas são? (HH:MM)\n')

#verifica se há dois pontos no lugar correto
if hora[2] == ':': dois_pontos=True
else: dois_pontos=False

#verificação formato 24h
hora_maior_que_0 = hora[0]>='0' and hora[1]>='0'
hora_menor_que_24 = (hora[0]=='2' and hora[1]<='4') or (hora[0]<='1')
minuto_maior_que_0 = hora[3]>='0' and hora[4]>='0'
minuto_menor_que_59 = hora[3]<='5' and hora[4]<='9'

if (hora_maior_que_0) and (hora_menor_que_24):
    hora_valida=True
else: hora_valida=False

if (minuto_maior_que_0) and (minuto_menor_que_59):
    minutos_validos=True
else: minutos_validos=False

#verifica o horário do dia para saudação correta
#se o horário informado for inválido, printa um erro!
dia = hora[0]<='1' and hora[1]<='1' or hora[0]=='0'   #00h às 11:59h
tarde = hora[0]=='1' and hora[1]<='7' and hora[1]>'1' #12 às 17:59h
noite = hora[0]>='1' and hora[1]>='8' or hora[0]>='2' #18h às 23:59h

if (hora_valida and minutos_validos and dois_pontos):
    if(dia): print('Bom dia!')
    elif (tarde): print('Boa tarde!')
    elif (noite): print('Boa noite!')
else: 
    print('\nhorário inválido')

#EXERCÍCIO 3
nome = input('Informe seu nome: ')
if len(nome)<=4:
    print('\nSeu nome é curto')
elif len(nome)==5 or len(nome)==6:
    print('\nSeu nome é normal')
else:
    print('\nSeu nome é muito grande')


