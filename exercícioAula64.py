nome = 'Marcelo Rodrigues'
# queremos deixar o nome como: *M*a*r*c*e*l*o* *R*o*d*r*i*g*u*e*s*

x=0 #caractere do nome que queremos adicionar à nova string
nova_string='*' #começa com asterisco

while x <= (len(nome)-1):       #começa no primeiro caractere e percorre o nome inteiro
    nova_string+= nome[x] + '*' #será sempre adicionado a nova string, cada caractere do nome + '*'
    x+=1                        #avança o caractere

print(nova_string)
