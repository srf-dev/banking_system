from datetime import datetime

NUMBER_OF_WITHDRAWALS = 3
bank_account = 1500.00
extract = []

selection = 0

while selection != 4:
    selection = int(input(f'''
        Escolha um tipo de operação:
            1 - Sacar (Quantidade de saques disponíveis: {NUMBER_OF_WITHDRAWALS})
            2 - Depositar
            3 - Ver Extrato
            4 - Sair
        '''                 
    ))
    if selection == 1:
        value = 0
        if NUMBER_OF_WITHDRAWALS > 0:
            while value <= 0 or value > bank_account:
                value = float(input("Digite o valor: "))
            
            value_update = bank_account - value
            bank_account = value_update

            print(f'O saque foi realizado com sucesso no valor de: R$ {value:.2f}') 
            date = datetime.now().strftime("%d/%m/%Y %H:%M")
            extract.append(f'[{date}] Saque realizado no valor de: R$ {value:.2f}')

            NUMBER_OF_WITHDRAWALS-=1
        else:
            print('Limite de saques esgotado! É permitido apenas 3 saques diários.')

    if selection == 2:
        value = 0
        while value <= 0:
            value = float(input("Digite o valor: "))

        value_update = bank_account + value
        bank_account = value_update
    
        print(f'O depósito foi realizado com sucesso no valor de: R$ {value:.2f}') 

        date = datetime.now().strftime("%d/%m/%Y %H:%M")
        extract.append(f'[{date}] Depósito realizado no valor de: R$ {value:.2f}')

    if selection == 3:
        print(f'''
        EXTRATO
        -----------------------------------------------
        Valor disponível em conta: R$ {bank_account}
        -----------------------------------------------
        ''')
        for activity in extract:
            print({activity}, end="\n")

print("Programa encerrado.")