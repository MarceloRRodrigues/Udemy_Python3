# F STRINGS --->
#limitando casas decimais no float
'''
pi = 3.14151787493029485
print(f'{pi:.2f}') #3,14
print(f'o numero de pi vale {pi}')

#FORMAT() -->
#igual a atribuição de variaveis no printf em C
#chaves {} seriam %, e .format() seriam as variáveis após aspas
pi = 3.14151787493029485
print('o numero e {:.2f}'.format(pi))

#CONDICIONAIS IFs --->

n1 = input('digite um numero')
n2 = input('digite outro numero')
soma = int(n1) + int(n2)

print(f'a soma é {soma}')
if(soma%2==0): 
    print('é par')
    print('tal coisa')
#endif
else:
    printd('talcoisa')
#endelse

#não são necessarios () e {}, apenas o : 
#a linha está dentro do IF/ELSE/ELIF quando tem um tab (4 caract) de margem 

#EXPRESSÕES LÓGICAS NO PRINT --->
print(True * False) #0
print(True and False) #False
print(True or False) #True
print(not False) #True
print(True + False) #1
#com operadores (+*-) retornará 0 ou 1
#com expressões (and,or,not) retornará True ou False

#OPERADORES IN E NOT IN -->
nome = input('Digite seu nome: ')
if 'a' in nome:
    print('tem "a" no nome')
elif ('a' not in nome):
    print('nao tem "a" no nome')

#INTERPOLAÇÃO DE STRINGS --->
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

# FORMATAÇÃO BÁSICA DE STRINGS -->
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')

FATIAMENTO DE STRINGS --->
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])

#TRY/EXCEPT -->
try:
    ...
except:
    ...
#diferente de um IF/ELSE, o try irá executar o código mesmo com
um erro, e se detectar erros, passa a executar o except.
o IF nem tenta executar código ao ver uma condição falsa, o try
vai até ver o erro

#FUNÇÃO ID -->
é a mesma coisa que endereço da variável na memória, em python seria a "identidade" da variável
é verificada coma função id(). ex:
var = 12
print(id(var))

#TIPOS IMUTÁVEIS
os imutáveis no python são: str, int, float, bool.
no código, ate podemos redefinir a variável onde armazenamos esses tipos de dados, mas não podemos alterá-los diretamente
ex:
nome = 'marcelo'
nome[6]='a' #acusará um erro, pois não é possível alterar o valor da variável, mas sim a variável
print(nome)
exemplo certo:
nome = 'Marcelo'
nome = 'Marcela'
print(nome) #Marcela (assim irá funcionar)

#CONTINUE e BREAK e ELSE
dentro de um laço while, if, for, etc... podemos ter -->

break: quebra o laço e sai do laço, executando o restante do código
continue: para de executar e volta desde o início do laço, executando novamente.

#FUNÇÕES DE STRING -->
existem muitas funções para strings que podem ser aplicadas direto do Python, como capitalize(), upper(), lower(), startswith()...
coloque um ponto no final de uma string e confira todas as opções e para que servem...

#EXCEPTION NO TRY EXCEPT
podemos definir a exception como uma variável, e imprimir essa variável para saber o que houve de errado
ex:
try
...
except Exception as error:
print(error)

além disso, podemos definir diferentes exceptions 

#WHILE/ELSE
while
    ...
else
    ...

o else será executado depois que a condição do while acabar, mas apenas se não houver um break.

#FOR IN-->
o laço for in percorrerá todos os caracteres de uma string, e armazena os valores em uma variável definida por vez.
strings são ITERÁVEIS, ou seja, te entregam um (1) valor por vez
ex:
texto = 'Bom dia!'

for letra in texto: print(letra)
#teremos cada letra printada na tela uma por vez

#FOR + RANGE -->
range -> range(start, stop, step) #começa em um número, para em outro, e pula a cada quantidade x de números.
o range também é ITERÁVEL
ex:
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero) #printa 0, e vai pulando a cada 8 números até chegar em 100, ou seja, multiplos de 8 menores que 100.

for numero in range(10):
    print(numero) #0;1;2;3;4;5;6;7;8;9

#ITERADOR -->
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)

#FUNÇÃO APPEND EM VETORES (adicionar elemento ao vetor)
lista = [1, 2, 3]  # Criando uma lista inicial

lista.append(4)  # Adicionando o número 4 ao final da lista

print(lista)  # Saída: [1, 2, 3, 4]
'''




