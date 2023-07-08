saldo = 0
saque = 0
extrato = ""
limite = 500
limite_saque = 3
n_saque = 0 

while True:

    opcao = int(input(f"""{'#'*10}MENU{'#'*10}
    [1] Depositar
    [2] Sacar 
    [3] Extrato
    [4] Sair
    """))


    if opcao == 1:
        valor = float(input('Digite o valor R$: '))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {saldo:.2f}\n"
        else:
            print("Operação Falhou! Valor incorreto")

    elif opcao == 2:
        n_saque += 1
        valor = float(input('Digite o valor R$: '))
        if valor > saldo:
            print("Saldo insuficiente" )
        elif  valor > limite:
            print("Excedido valor limite diário para saque")
        elif n_saque > limite_saque:
            print("Limite de saques diarios excedidos")
        else:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"

    elif opcao == 3:
            print(extrato)
    else:
        print("obrigado por utilizar nosso sistema")







