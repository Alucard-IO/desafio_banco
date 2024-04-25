menu = """
            ### Menu ###
           [d] Depositar
           [s] Sacar
           [e] Extrato
           [q] Sair
           #############
       """    

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:

    opçao = input(menu)

    if opçao == "d":
       deposito = float(input("Quanto deseja depositar? "))

       if deposito <= 0:
           print("Operação inválida, por favor informe uma quantidade maior que 0.")

       else: 
           saldo += deposito
           extrato += f"""  
           Déposito realizado no valor de R${deposito:.2f}.
           
           """

           print("Depósito realizado com sucesso.")

    elif opçao == "s": 

        saque = float(input(f""" 
        Este é seu saldo atual: R${saldo} reais.
                Quanto deseja sacar?  """))
        if saque <= saldo and numero_saques < LIMITE_SAQUES and saque <= limite:
            print("Saque realizado com sucesso.")
            saldo -= saque
            numero_saques += 1
            extrato += f"""
            Saque realizado no valor de R${saque:.2f}. 

            """
        elif saque > saldo:
            print("Saldo insuficiente.")

        elif numero_saques == LIMITE_SAQUES:
            print("Limite de saques diário atingido, por favor espere até amanhã.")

        elif saque > limite:
            print("Quantidade de saque maior que o limite permitido.")


    elif opçao == "e":
        if not extrato:
            print("Nenhuma movimentação foi realizada até o momento.")
        else:
            print(f"Saldo atual: R${saldo:.2f} ")    
            print(extrato)

    elif opçao == "q":
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida.")

print(menu)
        




         




