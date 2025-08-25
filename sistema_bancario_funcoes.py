menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

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
        valor_deposito = round(float(input("Informe o valor do depósito: ")), 2)
        print(f"Você solicitou depositar R$ {valor_deposito:.2f}")
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido. Informe um número maior que zero.")

    elif opcao == "s":
        print("Saque")

        if numero_saques >= LIMITE_SAQUES:
            print(f"Operação falhou! Número máximo de saques ({LIMITE_SAQUES}) atingido.")
        else:
            valor_saque = round(float(input("Informe o valor do saque: ")), 2)
            print(f"Você solicitou sacar R$ {valor_saque:.2f}")
            if valor_saque <= 0:
                print("Operação falhou! O valor informado é inválido. Informe um número maior que zero.")
            elif valor_saque > limite:
                print(f"Operação falhou! O valor máximo para saque é R$ {limite:.2f}.")
            elif valor_saque > saldo:
                print("Operação falhou! Saldo insuficiente.")
            else:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

    elif opcao == "e":
        print("\n", " Extrato ".center(40, "="), sep="")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=" * 40)

    elif opcao == "q":
        print("Sair...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
