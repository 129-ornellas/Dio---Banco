menu =  """
    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [q] - Sair

"""
saldo = 10
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':

        valor = float(input('valor de depósito: '))

        if valor <= 0:
            print('operação invalida, digite um valor positivo')
        
        else:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} \n"
            print("Depósito realizado")


    elif opcao == "s":
        valor_saque = float(input('valor à sacar: '))
        
        if valor_saque > limite:
            print("O valor desejado é maior que o limite por saque, insira um valor abaixo de R$ 500.00")
        elif numero_saques == LIMITE_SAQUES:
            print("Você excedeu o limite de saques diários.")
        elif valor_saque > saldo: 
            print("Não há saldo suficiente.")
        else:
            numero_saques +=1
            saldo -= valor_saque
            extrato += f"Saque de R$ {valor_saque:.2f} \n"
            print(f"Saque de {valor_saque:.2f} realizado")
        
    elif opcao == "e":
        if extrato == "":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações.")
        else:
            print("\n================ EXTRATO ================")
            print(extrato)
    
    elif opcao == "q":
        break
    else:
        print("Operação inválida, selecione uma das alterativas")