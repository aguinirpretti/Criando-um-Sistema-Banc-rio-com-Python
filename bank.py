menu = """

[D] Depositar
[E] Extrato
[S] Saque
[Q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = str(input(menu))

    if opcao == 'd':
        try:
            valor = float(input("\nInforme o valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("\nOperação falhou! O valor informado é inválido.")
        except ValueError:
            print("\nOperação falhou! Valor inválido. Certifique-se de inserir um número válido.")

    elif opcao == 's':
        try:
            valor = float(input("\nInforme o valor do saque: R$ "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("\nOperação falhou! Saldo insuficiente.")
            elif excedeu_limite:
                print("\nOperação falhou! O valor do saque excede o limite diário de 3 saques de R$ 500.00.")
            elif excedeu_saques:
                print("\nOperação falhou! Número de 3 saques diários atingidos.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f'\nSaque realizado no valor de: R${valor}')
            else:
                print("\nOperação falhou! O valor informado é inválido.")
        except ValueError:
            print("\nOperação falhou! Valor inválido. Certifique-se de inserir um número válido.")

    elif opcao == 'e':
        print("\n=================== EXTRATO =====================")
        print("\nNão foram realizaas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("\n=================== EXTRATO =====================")

    elif opcao == 'q':
        print("\nLogoff realizado")
        break

    else:
        print("\nOperação inválida! Escolha uma opção válida.")
