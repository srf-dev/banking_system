# Sistema Bancário com Orientação a Objetos em Python

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

Implementação de um sistema bancário orientado a objetos em Python, com uso de herança, polimorfismo e encapsulamento. Essa versão segue o paradigma de programação orientada a objetos (POO).

> 📌 Branch: `refactor/banking-system`

---

### ✔️ **Principais Componentes da Refatoração**

#### *Organização por Classes e Responsabilidades*

**Classes principais implementadas:**
- `Client`: representa o cliente do banco.
- `Account`: representa uma conta bancária.
- `Transaction`: classe base para operações.
- `Withdraw` / `Deposit`: herdam de `Transaction` e representam saques e depósitos.
- `History`: armazena o extrato da conta.
- `Menu`: interface de interação no terminal.

> O sistema utiliza **herança, polimorfismo, encapsulamento** e abstração com `abc.ABC`.

---

### **✔️ Detalhes das Classes**

#### `Client`
- Classe base para clientes
- Possui endereço e lista de contas
- Métodos:
  - `add_account(account)`
  - `do_transaction(account, transaction)`

#### `NaturalPerson(Client)`
- Cliente pessoa física
- Atributos:
- CPF, nome, data de nascimento, endereço

#### `Account`
- Classe base para contas
- Atributos:
  - agência, número da conta, saldo, cliente, histórico
- Métodos:
  - `withdraw(value)`
  - `deposit(value)`
  - `create_account(number, client)`

#### `CurrentAccount(Account)`
- Conta corrente com:
  - limite de R$ 500,00 por saque
  - máximo de 3 saques por dia
- Sobrescreve `withdraw(value)` para aplicar restrições

#### `History`
- Armazena transações
- Método:
  - `add_transaction(transaction)`

#### `Transaction (abstract)`
- Interface para transações
- Métodos abstratos:
  - `value`
  - `register(account)`

#### `Deposit(Transaction)`
- Representa um depósito
- Método `register(account)` chama `account.deposit`

#### `Withdraw(Transaction)`
- Representa um saque
- Método `register(account)` chama `account.withdraw`

---

### ✔️ **Interação via Terminal**

Menu interativo com as seguintes opções:

- [1] Sacar 
- [2] Depositar 
- [3] Ver Extrato 
- [4] Criar conta (Pessoa Física) 
- [5] Listar contas 
- [6] Criar novo usuário 
- [7] Sair
  

---

### Funções Auxiliares

```python
filter_clients(clients, cpf)   # Filtra cliente pelo CPF
list_accounts(accounts)        # Exibe informações das contas
create_client(clients)         # Cria um novo cliente
````



## Autor

Feito com 💜 por Shayare 🐈


