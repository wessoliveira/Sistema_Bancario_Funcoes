menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[u] Criar Usuário
[l] Listar Usuários
[c] Criar Conta
[k] Listar Contas

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

lista_usuarios = []
lista_contas = []

def Saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print(f"Saque de R$ {valor:.2f}!")
    if numero_saques >= limite_saques:
            print(f"Operação falhou! Número máximo de saques ({limite_saques}) atingido.")
    else:
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido. Informe um número maior que zero.")
        elif valor > limite:
            print(f"Operação falhou! O valor máximo para saque é R$ {limite:.2f}.")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def Deposito(saldo, valor, extrato, /):
    print(f"Depósito de R$ {valor:.2f}!")
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido. Informe um número maior que zero.")
    return saldo, extrato

def Extrato(saldo, /, *, extrato):
    print("\n", " Extrato ".center(40, "="), sep="")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=" * 40)

def Criar_Usuario(lista_usuarios):
    print("Criar Usuário")
    usuario = {}
    usuario['cpf'] = input("Informe o CPF (apenas números): ")
    lista_busca = [u for u in lista_usuarios if u['cpf'] == usuario['cpf']]
    if lista_busca:
        print("Usuário já existe!")
    else:
        usuario['nome'] = input("Informe o nome: ")
        usuario['data_nascimento'] = input("Informe a data de nascimento (dd/mm/aaaa): ")
        usuario['endereco'] = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        lista_usuarios.append(usuario)
        print("Usuário criado com sucesso!")
    return lista_usuarios

def Listar_Usuarios():
    print("\n", " Lista de Usuários ".center(40, "="), sep="")
    if not lista_usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for u in lista_usuarios:
            print(f"\n CPF: {u['cpf']}\n Nome: {u['nome']}\n Data de Nascimento: {u['data_nascimento']}\n Endereço: {u['endereco']}\n")
    print("=" * 40)

def Criar_Conta(lista_contas):
    print("Criar Conta")
    agencia = "0001"
    numero_conta = len(lista_contas) + 1
    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": None}
    cpf = input("Informe o CPF do usuário: ")
    lista_busca = [u for u in lista_usuarios if u['cpf'] == cpf]
    if lista_busca:
        conta['usuario'] = lista_busca[0]
        lista_contas.append(conta)
        print("Conta criada com sucesso!")
        print(f"Agência: {agencia}")
        print(f"Número da Conta: {numero_conta}")
    else:
        print("Usuário não encontrado, por favor verifique o CPF informado.")
    return lista_contas

def Listar_Contas():
    print("\n", " Lista de Contas ".center(40, "="), sep="")
    if not lista_contas:
        print("Nenhuma conta cadastrada.")
    else:
        for c in lista_contas:
            print(f"\n Agência: {c['agencia']}\n Número da Conta: {c['numero_conta']}\n Usuário: {c['usuario']['nome']} (CPF: {c['usuario']['cpf']})\n")
    print("=" * 40)

while True:

    opcao = input(menu)

    if opcao == "s":
        valor_saque = round(float(input("Informe o valor do saque: ")), 2)
        saldo, extrato, numero_saques = Saque(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    
    elif opcao == "d":
        valor_deposito = round(float(input("Informe o valor do depósito: ")), 2)
        saldo, extrato = Deposito(saldo, valor_deposito, extrato)
    
    elif opcao == "e":
        Extrato(saldo, extrato=extrato)

    elif opcao == "u":
        lista_usuarios = Criar_Usuario(lista_usuarios)

    elif opcao == "l":
        Listar_Usuarios()

    elif opcao == "c":
        lista_contas = Criar_Conta(lista_contas)

    elif opcao == "k":
        Listar_Contas()

    elif opcao == "q":
        print("Sair...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
