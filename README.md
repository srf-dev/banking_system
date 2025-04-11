# Simulador Básico de Sistema Bancário em Python

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

Resumo sobre os **comandos e funcionalidades implementados** com a proposta de modularização da **versão 2 do sistema bancário em Python**.

---

### ✔️ **Comandos Implementados**

#### *Modularização com Funções Separadas*

**Funções existentes separadas e refatoradas:**
- `withdraw_account`: função separada para saque.
- `deposit_account`: função separada para depósito.
- `show_extract`: função separada para exibir extrato.
<br><br>

> As funções seguem prática de passagem de parâmetros e uso de validações.

---

### **✔️ Descrição das Funções**

#### `withdraw_account(*, users, CPF, extract)`
- Recebe argumentos por **nome** (*keyword only*).
- Faz validação da conta, valor e quantidade de saques restantes.
- Atualiza saldo e extrato após o saque.
- Limite de 3 saques por dia por usuário.
- Limite de R$ 500,00 por saque.

#### `deposit_account(users, CPF, extract)`
- Recebe argumentos **por posição** (*positional-only*).
- Valida conta e valor.
- Atualiza saldo e extrato após depósito.

#### `show_extract(saldo, *, extrato)`
- Recebe `saldo` por posição e `extrato` por nome (*position and keyword only*).
- Exibe o histórico de movimentações se houver, senão mostra uma mensagem de extrato vazio.

---

### **✔️ Novas Funções Criadas**

#### `User.create()`
- Permite cadastrar um novo usuário.
- Valida se o CPF já está em uso.
- Armazena:
  - CPF (somente números)
  - Nome
  - Data de nascimento
  - Endereço (logradouro, número - bairro - cidade/estado)

> Evita cadastro duplicado por CPF.

---

#### `User.create_account(users, CPF)`
- Cria uma conta para um usuário já existente.
- Verifica se o CPF está cadastrado.
- Verifica se o número da conta já está vinculado a outro usuário.
- Vincula conta à lista `accounts` do usuário.

---

### **Outras Funcionalidades**

#### `User.data_user()`
- Retorna um dicionário com os dados do usuário e contas vinculadas.

#### Listagem de usuários
- Imprime dados de todos os usuários cadastrados, incluindo número de contas e agência.


---

### Branches de Desenvolvimento

| Branch                     | Descrição                                         | Status      | Link                                                                 |
|---------------------------|---------------------------------------------------|-------------|----------------------------------------------------------------------|
| `main`                    | Versão principal e estável                        | ✔️ Concluído | [Ver](https://github.com/srf-dev/banking_system/tree/main)     |
| `optimize/banking-system` | Refatoração e otimização do sistema bancário      | ✔️ Concluído | [Ver](https://github.com/srf-dev/banking_system/tree/optimize/banking-system) |
| `feature/new-api`         | Implementação de novas atualizações               | Planejando   | *em breve*                                                           |

---

## Autor

Feito com 💜 por Shayare 🐈

