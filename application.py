from datetime import datetime
import textwrap

def menu():
    menu =f"""
            ==================== MENU ====================

            Escolha um tipo de operação:

            [1] Criar novo usuário
            [2] Criar conta corrente
            [3] Listar usuários
            [4] Sacar
            [5] Depositar
            [6] Ver Extrato
            [7] Sair

            """
    return int(input(textwrap.dedent(menu)))

class User:
    def __init__(self, CPF, username, date_birth, address, bank_account, NUMBER_OF_WITHDRAWALS):
        self._CPF = CPF
        self.username = username
        self.date_birth = date_birth
        self.address = address

        self._bank_account = bank_account
        self._NUMBER_OF_WITHDRAWALS = NUMBER_OF_WITHDRAWALS
        self.AGENCY = '0001'
        self.accounts = []

    def data_user(self):
        return {
            "Nome": self.username,
            "Data_Nascimento": self.date_birth,
            "Endereco": self.address,
            "Agencia": self.AGENCY,
            "Contas": self.accounts
        }
    
    @classmethod
    def create(cls, users):
        while True:
            CPF = input("Digite seu CPF (Apenas Números!): ").strip()

            if not cls.validate_cpf(CPF):
                print('\n ⚠️  (ERRO) O CPF deve conter 11 digítos! Tente novamente. \n')
                continue
           
            if cls.user_manager(users, CPF):
                print('\n ⚠️  (ERRO) CPF já vinculado! Tente novamente. \n')
                continue
            
            username = input('Digite seu nome completo: ')
            date_birth = input('Digite a data do seu nascimento (dd/mm/aaaa): ')
            address = input('Digite seu endereço: (Logradouro, Número - Bairro - Cidade/Estado): ')
            bank_account = 0
            NUMBER_OF_WITHDRAWALS = 3

            return cls(CPF, username, date_birth, address, bank_account, NUMBER_OF_WITHDRAWALS)

    @staticmethod
    def validate_cpf(CPF):
        return len(str(CPF)) == 11

    @staticmethod
    def user_manager(users, CPF):
        for user in users:
            if user._CPF == CPF:
                return True
        return False
    
    @staticmethod
    def create_account(users, CPF):
        if not users:
            print(textwrap.dedent('''
            -----------------------------------------------
                   ❌ Não há usuários cadastrados!
            -----------------------------------------------                                
            '''))
            return
            

        for user in users:
            if user._CPF == CPF:
                account_number = int(input(textwrap.dedent('''
                -----------------------------------------------
                                Criar conta 
                -----------------------------------------------
                            
                Digite o número da conta bancária:
                                        
                ''')))

                accounts = user.accounts

                if account_number in accounts:
                    print(textwrap.dedent('''
                    -----------------------------------------------
                          Conta já vinculada com seu usuário!
                    -----------------------------------------------                                            
                    '''))
                elif any(account_number in us.accounts for us in users if us._CPF != CPF):
                          print(textwrap.dedent('''
                    -----------------------------------------------
                       ❌ Conta já vinculada com outro usuário!
                    -----------------------------------------------                                            
                    '''))              
                else:
                    user.accounts.append(account_number)
                    print(textwrap.dedent('''
                    -----------------------------------------------
                            ✅ Conta criada com sucesso!
                    -----------------------------------------------                                
                    '''))
                return

        print(textwrap.dedent('''
        -----------------------------------------------
         ❌ Não há usuários cadastrados com esse CPF!
        -----------------------------------------------                                
        '''))
                    
def withdraw_account(users, /, CPF, *, extract):
    withdrawal_limit = 500.00

    for user in users:
        if user._CPF == CPF:
            accounts = user.accounts
            account_number = int(input('\n Digite o número da conta: \n'))

            if account_number in accounts:
                value = 0
                if user._NUMBER_OF_WITHDRAWALS > 0:
                    
                    while value <= 0 or value > user._bank_account:
                        selection = int(input(textwrap.dedent('''
                        -----------------------------------------------
                                            Opções
                        -----------------------------------------------
                        
                        Digite:
                        [1] Para continuar
                        [2] Para sair
                                    
                        ''')))

                        if selection == 1:
                            value = float(input("\n Digite o valor: \n"))

                            if value <= 0:
                                print('\n ❌  Valor inválido! Não é permitido valores negativos. \n')
                            elif value > user._bank_account:
                                print('\n ❌  Valor inválido! Saldo insuficiente em conta. \n')
                            elif value > withdrawal_limit:
                                print(f'\n ❌  Valor inválido! O valor máximo para saque é de R$ {withdrawal_limit} \n')
                            else:
                                print(f'\n ✅ O saque foi realizado com sucesso no valor de: R$ {value:.2f} \n')
                                date = datetime.now().strftime("%d/%m/%Y %H:%M")
                                extract.append(f"[{date}] [Agência: {user.AGENCY}] [Conta: {account_number}] ✅ Saque realizado por {user.username} no valor de: R$ {value:.2f}")

                                user._bank_account -= value

                                user._NUMBER_OF_WITHDRAWALS-=1
                        elif selection == 2:
                            break
                        else:
                            print('\n Opção inválida! Digite novamente. \n')
                else:
                    print('\n ❌ Limite de saques esgotado! É permitido apenas 3 saques diários. \n')
                break
            else:
                print('\n ❌  (Conta inválida!) A conta inserida não está registrada. \n')
                break                   
    else:
        print(textwrap.dedent('''
        -----------------------------------------------
                O CPF inserido não está registrado!
        -----------------------------------------------
        '''))

def deposit_account(users, CPF, extract):
        for user in users:
            if user._CPF == CPF:
                accounts = user.accounts
                account_number = int(input('\n Digite o número da conta: \n'))

                if account_number in accounts:

                    selection = int(input(textwrap.dedent('''
                    -----------------------------------------------
                                        Opções
                    -----------------------------------------------
                            
                    Digite:
                    [1] Para continuar
                    [2] Para sair
                                        
                    ''')))

                    if selection == 1:
                        value = float(input("Digite o valor: "))

                        if value <= 0:
                            print('\n ❌  Valor inválido! Não é permitido valores negativos. \n')
                        else:
                            print(f'\n ✅ Depósito realizado com sucesso no valor de: R$ {value:.2f} \n')
                            date = datetime.now().strftime("%d/%m/%Y %H:%M")
                            extract.append(f"[{date}] [Agência: {user.AGENCY}] [Conta: {account_number}] ✅ Depósito realizado por {user.username} no valor de: R$ {value:.2f}")

                            user._bank_account += value

                    elif selection == 2:
                        break
                    else:
                        print('\n Opção inválida! Digite novamente. \n')                   
                else:
                    print('\n ❌  (Conta inválida!) A conta inserida não está registrada. \n')  

                return
        
        print(textwrap.dedent('''
        -----------------------------------------------
             O CPF inserido não está registrado!
        -----------------------------------------------
        '''))

def show_extract(extract):
        
        if extract:
            print(textwrap.dedent(f'''
                                  
            -----------------------------------------------
                                EXTRATO
            -----------------------------------------------
            
            '''))
            for activity in extract:
                print({activity}, end="\n")
        else:
            print(textwrap.dedent(f'''
                                  
            ------------------------------------------------
             Ainda não foi realizando nenhuma novimentação!
            ------------------------------------------------
            
            '''))

def main():
    users = []
    extract = []

    while True:
        selection = menu()

        if selection == 1:
            new_user = User.create(users)
            users.append(new_user)
            print(textwrap.dedent('''
                                  
                ------------------------------------
                  ✅ Usuário criado com sucesso!
                ------------------------------------
                                  
                  '''))
        
        elif selection == 2:
            CPF = input('Digite seu CPF: ')
            User.create_account(users, CPF)

        elif selection == 3:
            if not users:
                print(textwrap.dedent('''
                                  
                -----------------------------------------------
                  ❌ Não há usuários cadastrados no sistema!
                -----------------------------------------------
                                  
                  '''))
            else:
                print(textwrap.dedent('''
                -----------------------------------------------
                        Usuários cadastrados no sistema:
                -----------------------------------------------
                '''))

                for user in users:
                    data = user.data_user()
                    print(f'\n'.join(f'{key}: {value}' for key, value in data.items()),'\n')
                    print("-" * 55 + "\n")


        elif selection == 4:
            CPF = input('Digite seu CPF: ')
            withdraw_account(users, CPF, extract=extract)

        elif selection == 5:
            CPF = input('Digite seu CPF: ')
            deposit_account(users, CPF, extract)

        elif selection == 6:
            show_extract(extract)

        elif selection == 7:
            print('Programa encerrado!')
            break
        else:
            print("\n ⚠️  Opção não implementada. Digite uma opção válida! \n")
main()