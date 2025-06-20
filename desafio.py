import textwrap

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar usuário
    [c] Cadastrar conta
    [l] Listar contas
    [q] Sair
    => """
    return input(textwrap.dedent(menu))
    
def saque(*,saldo,valor,extrato,limite,numero_saques, limite_saques):   

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, extrato, numero_saques

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, extrato, numero_saques

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato, numero_saques

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques      

    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques 
    
def deposito( valor, extrato, saldo,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        

    else:
            print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def relatorio(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF(somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"CPF{cpf} já está cadastrado")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaa): ")
    endereco = input("Digite seu endereço(Rua, numero - Bairro - cidade/Sigla stado): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

    print("Novo usuario cadastrado")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Digite o CPF(somente numeros): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    
    print(f"Usuário {cpf} não encontrado: ")

def listar_contas(contas):
    for conta in contas:
        linha = """
            Agência: {conta["agencia"]}
            C/C: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        
        
def main():

    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0    
    usuarios =[]
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(valor, extrato, saldo)            

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques= saque(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )            

        elif opcao == "e":
            relatorio(saldo, extrato=extrato)            

        elif opcao == "q":
            break

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "l":
            listar_contas(contas)            

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()