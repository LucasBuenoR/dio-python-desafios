# importa configurações do sistema
import os

from datetime import datetime

# comando para limpar o terminal
os.system("clear")


# listas e variaveis
historico_deposito = []
historico_saque = []
saldo = 0
numero_saques = 0
limite = 500
# novas
transacoes_hoje = 0
LIMITE_TRANSACOES_DIARIAS = 10


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


def op_deposito():
    global saldo, transacoes_hoje

    if transacoes_hoje >= LIMITE_TRANSACOES_DIARIAS:
        print("Limite diário de transações atingido (10 transações por dia).")
        return

    valor_deposito = float(input("Informe o valor a ser depositado: "))
    if valor_deposito <= 0:
        print("Valor do deposito precisa ser maior que R$0")

    else:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        historico_deposito.append((valor_deposito, data_hora))
        saldo += valor_deposito
        transacoes_hoje += 1
        print(f"O valor depositado foi de + R${valor_deposito} em {data_hora}")


def op_saque():
    LIMITE_SAQUE = 3
    global  numero_saques, saldo, limite, transacoes_hoje

    if transacoes_hoje >= LIMITE_TRANSACOES_DIARIAS:
        print("Limite diário de transações atingido (10 transações por dia).")
        return

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
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        historico_saque.append((valor_saque, data_hora))
        saldo -= valor_saque
        numero_saques += 1
        transacoes_hoje += 1
        print(f"O valor sacado foi de - R${valor_saque} em {data_hora}")


def exibi_extrato():
    global saldo
    if not historico_deposito and not historico_saque:
        print("Nenhum depósito ou saque foi realizado.")
    else:
        print("Extrato de transações:")
        for valor, data_hora in historico_deposito:
            print(f"+ R${valor} em {data_hora}")
        for valor, data_hora in historico_saque:
            print(f"- R${valor} em {data_hora}")
        print(f"Saldo atual: R$ {saldo}")

menu_de_opcoes()


