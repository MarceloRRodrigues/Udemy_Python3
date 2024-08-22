print('Bem-vindo à calculadora')
while True:
    n1= input('Digite o primeiro número: ')
    n2= input('Digite o segundo número: ')
    num1 = float(n1)
    num2 = float(n2)
    if n1 is not float or n2 is not float:
        print("Numero(s) inválido(s). Entre com números reais.")
        continue
    
    operacao= input('Digite a operacao (* + - /): ')
    if operacao=='*': print(num1*num2)
    elif operacao=='+': print(num1+num2)
    elif operacao=='-': print(num1-num2)
    elif operacao=='/': print(num1/num2)
    else: print('Operação inválida')

    opcao = input('\nDeseja sair? Se SIM, digite "S", se NÃO, digite qualquer tecla: ')
    if opcao == 'S' or opcao == 's': break
print('Você saiu.')
