saldo = 0
extrato_saque = []
extrato_deposito = []
opcao = 0


while opcao != 4:

    print("MENU".center(28, "#"))
    print('''
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair
    ''')
    print("".center(28, "#"))

    opcao = int(input('\nDigite a opção desejada: '))

    if opcao == 1:
        deposito = int(input("Digite um valor a ser depositado:\nR$ "))
        extrato_deposito.append(deposito)
        saldo += deposito
    elif opcao == 2:
        valorSaque =  int(input("Qual valor você gostaria de sacar?\nR$ "))
        if valorSaque > 500:
            print("Valor de saque maior que o limite diário de R$ 500,00. Por favor tente novamente.")
        elif saldo < valorSaque:
            print('Saldo insuficiente!!!')
        else:
            saldo -= valorSaque
            print(f'Saque efetuado com sucesso.')
            extrato_saque.append(valorSaque)

    elif opcao == 3:

        if not extrato_deposito:
            print('Não foram realizadas movimentações na conta.\n\n')

        else:

            for i in extrato_deposito:
                print(f'Depósito efetuado: R$ {i:.2f}\n')

            for i in extrato_saque:
                print(f'Saque efetuado: {i:.2f}\n')

            print(f'O seu saldo atual é de R$ {saldo:.2f}\n')
    elif opcao == 4:
        break






