menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
num_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")

        else:
            print("Operação falhou! O valor é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))

        exced_saldo = valor > saldo
        exced_limite = valor > limite
        exced_saque = num_saque >= LIMITE_SAQUES

        if exced_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif exced_limite:
            print("Operação falhou! O valor do saque excede o Limite.")
        
        elif exced_saque:
            print("Operação Falhou! Número máximo de saques excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saque += 1
            print("Saque realizado com sucesso.")

        else:
            print("Operação falhou! O valor infmorado é invalido.")

    elif opcao == "e":
        print("\n =============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")