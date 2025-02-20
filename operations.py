"""
    _summary_

    Este é um projeto proposto pelo bootcamp "Suzano - Python Developer" da Digital Innovation One.
    O objetivo é criar um sistema bancário simples, com funções de depósito, saque e extrato.
    Este arquivo contém as funções de depósito e saque.

    Args:
        saldo (float): Saldo da conta.
        extrato (str): Extrato da conta.
        saque_maximo (float): Valor máximo permitido para saque.
        saques_disponiveis (int): Número de saques disponíveis.
    
    funções:
        deposito(saldo, extrato): Função para realizar um depósito.
        saque(saldo, extrato, saque_maximo, saques_disponiveis): Função para realizar um saque.
"""

# Função para realizar um depósito
def deposito(saldo, extrato):
    while True:
        try:
            deposito = float(input("Digite o valor do depósito: "))
            if deposito <= 0: # Verifica se o valor do depósito é válido
                    print("Por favor, digite um valor maior que zero.")
                    continue
            elif deposito > 0: # Realiza o depósito
                    saldo += deposito
                    extrato += f"Depósito: +R$ {deposito:.2f}\n"
            return saldo, extrato
            break

        except ValueError:
            print("Por favor, digite um valor numérico válido.")
            continue

# Função para realizar um saque
def saque(saldo, extrato, saque_maximo, saques_disponiveis):
    print(f"Você tem {saques_disponiveis} saques disponíveis e seu saldo é de R$ {saldo:.2f}.")
    if saldo == 0 or saques_disponiveis == 0: # Verifica se é possível realizar um saque
        print("Não é possível realizar um saque.")
        return saldo, extrato, saque_maximo, saques_disponiveis
    
    elif saldo > 0 and saques_disponiveis > 0:
        while True:
            try:
                saque = float(input("Digite o valor do saque: "))
                if saque > saldo or saque > saque_maximo or saque <= 0: # Verefica as condicionais para saque
                    print("Valor de saque inválido.")
                    continue
                elif saque <= saldo and saque <= saque_maximo:
                     saldo -= saque
                     saques_disponiveis -= 1
                     extrato += f"Saque: -R$ {saque:.2f}\n"
                     return saldo, extrato, saque_maximo, saques_disponiveis                     
            
            except ValueError: # Tratamento de exceção
                print("Por favor, digite um valor numérico válido.")
                continue
                
