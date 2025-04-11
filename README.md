# Simulador Básico de Sistema Bancário em Python

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

## Sobre

Este projeto é um **simulador de sistema bancário** desenvolvido como desafio proposto pela **DIO**. O objetivo foi aplicar conceitos de programação em Python aprendidos, como:

- Funções
- Estruturas condicionais
- Laços de repetição
- Manipulação de variáveis

O sistema permite ao usuário realizar **operações bancárias simples**, como **depósito**, **saque** e **visualização de extrato**.

---

## Pré-requisitos

- Python 3 instalado na máquina
- Terminal, prompt de comando ou IDE (como VS Code)

---

## Como instalar

Via terminal (Git Bash, cmd, etc.):

1. Acesse o diretório onde deseja clonar o repositório:

```bash
cd /caminho/do/seu/diretorio
```

2. Clone o repositório:

```bash
git clone https://github.com/srf-dev/banking_system.git
```

3. Acesse a pasta do projeto:

```bash
cd repositorio
```

4. Execute o script:

```bash
python application.py
```

---

## Como utilizar

Ao iniciar o programa, o usuário verá um menu com as opções disponíveis:

- `1` para saque
- `2` para depósito
- `3` para extrato
- `4` para sair

O sistema inicia com um saldo fictício de **R$ 1500,00** (valor que pode ser alterado diretamente no código).

---

## Funcionalidades

- **Depósito** de valores positivos
- **Saque** com limite de 3 operações por sessão
- **Mensagem de erro** para saques com saldo insuficiente
- **Extrato** com o histórico completo das operações e saldo atual
- **Interface simples** via terminal

---

## Regras implementadas

- Não é possível depositar valores negativos ou zerados
- Máximo de **3 saques** por execução do programa
- Saques só são permitidos se houver **saldo suficiente**
- O extrato exibe **todas as movimentações** e o **saldo final**

---

## Exemplo de uso

```bash
[1] Sacar
[2] Depositar
[3] Ver Extrato
[4] Sair
=> 1
Digite o valor: 10

O depósito foi realizado com sucesso no valor de: R$ 10,00

=> 3
EXTRATO
-----------------------------------------------
Valor disponível em conta: R$ 1490.0 
-----------------------------------------------
{'[05/04/2025 01:46] Saque realizado no valor de: R$ 10.00'}
```

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

