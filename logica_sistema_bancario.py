menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3       


while True:
    opcao = input(menu)
    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))
        if  valor > 0:
            saldo += valor
            extrato += f"valor depositado: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")


    
    elif opcao == "s":
        numero_saques += 1
        if numero_saques > LIMITE_SAQUES:
            print("Número máximo de saques diários atingido")
            continue
        print("Saque")
        valor_saque = float(input("informe o valor de saque:"))
        if valor_saque > saldo:
            print("saldo insuficiente")
        elif valor_saque > limite:
            print("valor acima do limite")                 
        else:
            saldo -= valor_saque
            extrato += f"valor sacado: R$ {valor_saque:.2f}\n"
            print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
   
           
         

    elif opcao =="e":
        print("Extrato")
        if not extrato:
            print("Nenhum valor movimentado")
        else:
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")


    elif opcao == "q":
        print("Saindo...")
        break