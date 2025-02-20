"""_summary_
    Este é um projeto proposto pelo bootcamp "Suzano - Python Developer" da Digital Innovation One.
    O objetivo é criar um sistema bancário simples, com funções de depósito, saque e extrato.
    Este arquivo contém o código principal do projeto.

    Args:
        saldo (float): Saldo da conta.
        extrato (str): Extrato da conta.
        saque_maximo (float): Valor máximo permitido para saque.
        saques_disponiveis (int): Número de saques disponíveis.
    
    funções:
        deposito(saldo, extrato): Função para realizar um depósito.
        saque(saldo, extrato, saque_maximo, saques_disponiveis): Função para realizar um saque.
"""

# Importa o módulo operations
import operations

# Mensagens iniciais
mensagem_inicio = """Serviço Bancario"""
mensagem_operações= """Escolha uma operação:
1 - Depósito
2 - Saque
3 - Extrato
4 - Sair
\n
"""

# Variáveis iniciais
saldo = 0
extrato = ""
saque_maximo = 500
saques_disponiveis = 3

########################################################################################

# Início do programa

while True:

    print(mensagem_inicio.strip().center(50, "-"))
    print(mensagem_operações.strip())

    operacao = input("Digite o número da operação desejada: ")

    if operacao == "1":
        saldo, extrato = operations.deposito(saldo, extrato)
    
    elif operacao == "2":
        saldo, extrato, saque_maximo, saques_disponiveis = operations.saque(saldo, extrato, saque_maximo, saques_disponiveis)

    elif operacao == "3":
        print("Dados bancários".center(50, "-"), f"""\n
            Seu extrato:\n\n{extrato}""",f"\nSaldo: R$ {saldo:.2f}","\n","-".center(50, "-"), "\n")
        
    elif operacao == "4":
        print("Obrigado por utilizar nossos serviços.")
        exit()
        break

    else:
        print("Operação inválida.")
        continue
        

