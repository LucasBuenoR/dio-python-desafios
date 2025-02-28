# importa configurações do sistema
import os
# comando para limpar o terminal
os.system("clear")

# funcao menu de opcoes


def menu_de_opcoes():
    opcoes = """
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair
    => """

    while True:
        opcao = input(opcoes)

        # chama a funcao op_deposito
        if opcao == "1":
            print("Deposito")
            op_deposito()

        # chama a funcao op_saque
        elif opcao == "2":
            print("Saque")
            op_saque()

        # chama a funcao exibi_extrato
        elif opcao == "3":
            print("Extrato")
            exibi_extrato()

        # enquanto o usuario nao escolher a opcao 0 o laço não para executar
        elif opcao == "0":
            print("Saindo...")
            break

        # qualquer tecla fora do escopo de opcoes e apresentado o print a baixo
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# listas e variaveis
historico_deposito = []
historico_saque = []
saldo = 0
numero_saques = 0
limite = 500


def op_deposito():
    global saldo, historico_deposito

    valor_deposito = float(input("Informe o valor a ser depositado: "))
    if valor_deposito <= 0:
        print("Valor do deposito precisa ser maior que R$0")

    else:
        historico_deposito.append(valor_deposito)
        saldo += valor_deposito
        print(f"o valor deposito foi de + R${valor_deposito}")


def op_saque():
    LIMITE_SAQUE = 3
    global historico_saque, numero_saques, saldo, limite

    if numero_saques >= LIMITE_SAQUE:
        print("Limite diário de saques atingido (3 saques por dia).")
        return

    valor_saque = float(input("Informe o valor a ser sacado: "))
    if valor_saque <= 0:
        print("Valor do saque precisa ser maior que R$0")

    elif valor_saque > limite:
        print("O valor do saque não pode ser maior que R$500")

    elif valor_saque > saldo:
        print("Saldo insuficiente para realizar o saque.")

    else:
        historico_saque.append(valor_saque)
        saldo -= valor_saque
        numero_saques += 1
        print(f"o valor saque foi de - R${valor_saque}")


def exibi_extrato():
    global saldo
    if not historico_deposito and not historico_saque:
        print("Nenhum depósito ou saque foi realizado.")
    else:
        print("Extrato de transações:")
        for valores in historico_deposito:
            print(f"+ R${valores}")
        for valores in historico_saque:
            print(f"- R${valores}")
        print(f"Saldo atual: R$ {saldo}")


menu_de_opcoes()
