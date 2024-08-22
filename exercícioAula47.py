nome = input('Digite seu nome: ');
idade = input('\nDigite sua idade: ')
if nome == '' or idade == '':
    print('\nDesculpe, você deixou campos vazios.')
else:
    if ' ' in  nome: espaco='contém'
    else: espaco='não contém'

    print(f'\nSeu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[-(len(nome))]}')
    print(f'A última letra do seu nome é {nome[-1]}')