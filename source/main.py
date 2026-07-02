import threading
from sistema import sacar, ver_saldo, depositar, transferir

def operacao():
    sacar(1, 100)

def teste_concorrencia():
    threads = []

    for i in range(5):
        t = threading.Thread(target=operacao)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Teste de concorrência finalizado!")

def menu():
    while True:
        print("\n========== SISTEMA BANCÁRIO ==========")
        print("1 - Ver saldo")
        print("2 - Sacar")
        print("3 - Depositar")
        print("4 - Transferir entre contas")
        print("5 - Testar concorrência")
        print("6 - Sair")
        print("======================================")

        op = input("Escolha uma opção: ")

        if op == "1":
            conta = int(input("Digite o ID da conta: "))
            ver_saldo(conta)

        elif op == "2":
            conta = int(input("Digite o ID da conta: "))
            valor = float(input("Digite o valor do saque: R$ "))
            sacar(conta, valor)

        elif op == "3":
            conta = int(input("Digite o ID da conta: "))
            valor = float(input("Digite o valor do depósito: R$ "))
            depositar(conta, valor)

        elif op == "4":
            origem = int(input("Conta de origem: "))
            destino = int(input("Conta de destino: "))
            valor = float(input("Valor da transferência: R$ "))
            transferir(origem, destino, valor)

        elif op == "5":
            print("\nIniciando teste de concorrência...")
            teste_concorrencia()

        elif op == "6":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida!")
