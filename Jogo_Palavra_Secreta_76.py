"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'chromatica'              #definição da palavra (editar conforme o desejado)
palavra_escondida = ''                      #é a palavra com asteriscos, conforme vai sendo adivinhada
tentativas = 0                              #variável que armazena tentativas (começa em 0)
vetor = []                                  #vetor que armazena os caracteres mutáveis que serão substituídos conforme adivinhados
for carac in palavra_secreta:               
    vetor.append('*')                       #preenche o vetor com asteriscos inicialmente (conforme tamanho da palavra secreta)

print('Palavra secreta: ',end='')           #printa a quantidade de letras da palavra secreta no início
for posicao in vetor:
    print(posicao,end='')

while palavra_escondida != palavra_secreta: #enquanto a palavra não for adivinhada por completo...

    posicao = 0                             #índice que percorre o vetor da palavra escondida
    print('\n')
    print(f'Tentativas até o momento = {tentativas}')                  #printa quantas tentativas já foram realizadas
    letra = input("Digite uma letra:")                                 #recebe a letra
    if (letra.isalpha()) and len(letra)==1:                            #se a informação recebida for apenas UMA letra...
        tentativas+=1                                                  #incrementa o número de tentativas
        for caractere in palavra_secreta:                              #para todo o caractere na palavra secreta...
            if letra == caractere:                                     #se a letra adivinhada for igual a um caractere na apalvra secreta...
                vetor[posicao] = letra                                 #o vetor armazena a letra adivinhada na posição correspondente 
            posicao+=1                                                 #incrementa a posição
    else:
        print('Não é uma letra válida')     #se a informação recebida não for letra e APENAS 1 letra, inválido
        continue                            #retorna ao início do loop
    print('\n')
    palavra_escondida = ''.join(vetor)      #armazena as posições do vetor na palavra escondida em formato de string
    print('Palavra secreta: ',end='')       #printa a palavra secreta com as letras já adivinhadas
    for posicao in vetor:
        print(posicao,end='')

print("\nPARABÉNS!! Você acertou! :)")      #se a palavra foi adivinhada...