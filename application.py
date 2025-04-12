from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Client():
    def __init__(self, address):
        self.address = address
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)

    def do_transaction(self, account, transaction):
        transaction_success = transaction.register(account)
        if transaction_success:
            account.history.add_transaction(transaction)

class NaturalPerson(Client):
    def __init__(self, cpf, name, date_birth, address):
        super().__init__(address)
        self.cpf = cpf
        self.name = name
        self.date_birth = date_birth


class Account():
    def __init__(self, number, client):
        self._AGENCY = '0001'
        self._balance = 0
        self._number = number
        self._client = client
        self._history = History()

    @classmethod
    def create_account(cls, number, client):
        account = cls(number, client)
        client.add_account(account)
        return account
    
    @property
    def agency(self):
        return self._AGENCY
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def number(self):
        return self._number
    
    @property
    def client(self):
        return self._client
    
    @property
    def history(self):
        return self._history

    def withdraw(self, value):
        if value > self._balance:
            print('\n ❌ (ERRO) Valor de saldo excedido!  \n')
            return False

        if value <= 0:
            print('\n ❌ (ERRO) O valor digitado é inválido!  \n')
            return False

        self._balance -= value
        print('\n ✅ Saque realizado com sucesso!  \n')
        return True

    def deposit(self, value): 
        if value <= 0:
            print('\n ❌ (ERRO) O valor digitado é inválido!  \n')
            return False

        self._balance += value
        print('\n ✅ Depósito realizado com sucesso!  \n')
        return True

class CurrentAccount(Account):
    def __init__(self, number, client, number_of_withdrawals=3, withdrawal_limit=500):
        super().__init__(number, client)
        self._number_of_withdrawals = number_of_withdrawals
        self._withdrawal_limit = withdrawal_limit
    
    def withdraw(self, value):
        number_of_withdrawals = len([t for t in self.history.transactions if t["tipo"] == 'Withdraw'])
        
        if value > self._withdrawal_limit:
            print('\n ❌ (ERRO) Valor excede o limite por saque! \n')
            return False

        if number_of_withdrawals >= self._number_of_withdrawals:
            print('\n ❌ (ERRO) Número máximo de saques excedido! \n')
            return False

        return super().withdraw(value)

class Transaction(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def register(self, account):
        pass

class History():
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions
    
    def add_transaction(self, transaction):
        self._transactions.append({
            "tipo": transaction.__class__.__name__,
            "valor": transaction.value,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        return account.deposit(self._value)

class Withdraw(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        return account.withdraw(self._value)

def filter_clients(clients, cpf):
    filtered_client = [client for client in clients if client.cpf == cpf]
    return filtered_client[0] if filtered_client else None

def list_accounts(accounts):
    for account in accounts:
        print(f"""
            Agência: {account.agency}
            Conta: {account.number}
            Titular: {account.client.name}
        """)

def create_client(clients):
    cpf = input('\n Digite o CPF (Apenas números): \n')
    client = filter_clients(clients, cpf)

    if client:
        print('\n ❌ (ERRO) CPF já vinculado!  \n')
        return
    
    name = input('Digite seu nome completo: ')
    date_birth = input('Digite a data do seu nascimento (dd/mm/aaaa): ')
    address = input('Digite seu endereço: (Logradouro, Número - Bairro - Cidade/Estado): ')

    client = NaturalPerson(cpf=cpf, name=name, date_birth=date_birth, address=address)

    clients.append(client)

    print('\n ✅ Cliente criado com sucesso!  \n')

def create_account(accounts, clients, number):
    cpf = input('\n Digite o CPF (Apenas números): \n')
    client = filter_clients(clients, cpf)

    if not client:
        print('\n ❌ (ERRO) Não há clientes registrados com esse CPF! \n')
        return

    account = CurrentAccount(number, client)
    client.add_account(account)
    accounts.append(account)
    print('\n ✅ Conta criada com sucesso! \n')

def request_withdrawal(clients):
    cpf = input('\n Informe o CPF: ')
    client = filter_clients(clients, cpf)

    if not client:
        print('\n ❌ Cliente não encontrado.')
        return

    value = float(input('Informe o valor do saque: '))
    account = client.accounts[0]
    transaction = Withdraw(value)
    client.do_transaction(account, transaction)

def request_deposit(clients):
    cpf = input('\n Informe o CPF: ')
    client = filter_clients(clients, cpf)

    if not client:
        print('\n ❌ Cliente não encontrado.')
        return

    value = float(input('Informe o valor do depósito: '))
    account = client.accounts[0]
    transaction = Deposit(value)
    client.do_transaction(account, transaction)

def show_statement(clients):
    cpf = input('\n Informe o CPF: ')
    client = filter_clients(clients, cpf)

    if not client:
        print('\n ❌ Cliente não encontrado.')
        return

    account = client.accounts[0]
    print(f"\n ===== EXTRATO da conta {account.number} =====")
    for t in account.history.transactions:
        print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
    print(f"\nSaldo atual: R$ {account.balance:.2f}")
    print("="*40)

def menu():
    menu =f"""
            ==================== MENU ====================

            Escolha um tipo de operação:

            [1] Sacar
            [2] Depositar
            [3] Ver Extrato
            [4] Criar conta (Pessoa Física)
            [5] Listar contas
            [6] Criar novo usuário
            [7] Sair

            """
    return int(input(textwrap.dedent(menu)))

def main():
    clients = []
    accounts = []

    while True:
        selection = menu()

        if selection == 1:
            request_withdrawal(clients)
        
        elif selection == 2:
            request_deposit(clients)

        elif selection == 3:
            show_statement(clients)

        elif selection == 4:
            number = len(accounts) + 1
            create_account(accounts, clients, number)       

        elif selection == 5:
            list_accounts(accounts)

        elif selection == 6: 
            create_client(clients)

        elif selection == 7:
            print('\n ✅ Saindo do sistema...\n')
            break

        else:
            print('\n ❌ Opção inválida. Tente novamente. \n')

main()
