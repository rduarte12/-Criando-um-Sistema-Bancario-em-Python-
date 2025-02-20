# README - Sistema Bancário

## Descrição

Este projeto é proposto pelo bootcamp "Suzano - Python Developer" da Digital Innovation One. O objetivo é criar um sistema bancário simples, com funções de depósito, saque e extrato.

## Explicando o projeto

-Para fins de organização de leitura do código e demonstração de conhecimentos, as funções principais foram sepearadas em um segundo arquivo, denominado 'operations.py'.

-O código principal está em 'main.py'

## Como Executar

1. Clone o repositório para sua máquina local.
2. Certifique-se de ter o Python instalado.
3. Execute o arquivo principal para iniciar o sistema bancário.

## Pseudocódigo

```plaintext
INÍCIO do programa

    EXIBIR mensagens iniciais
    DEFINIR variáveis iniciais (saldo, extrato, saque máximo, saques disponíveis)

    ENQUANTO Verdadeiro:
        SOLICITAR ao usuário que escolha uma operação (1-Depósito, 2-Saque, 3-Extrato, 4-Sair)
        
        SE a operação for 1 (Depósito):
            CHAMAR a função de depósito
        SENÃO SE a operação for 2 (Saque):
            CHAMAR a função de saque
        SENÃO SE a operação for 3 (Extrato):
            EXIBIR extrato da conta
        SENÃO SE a operação for 4 (Sair):
            EXIBIR mensagem de saída e encerrar o programa
        SENÃO:
            EXIBIR mensagem de operação inválida e solicitar novamente

FIM do programa´´´

## Explicando as funções

- 'deposito()': Função que verifica a possibilidade e, caso possível, realiza o depósito na conta.
- 'saque()'   : Função que verifica a possibilidade e, caso possível, realiza o saque da conta.

##Tecnologias Utilizadas
- Python

###Autor
Desenvolvido por [@rduarte12](https://github.com/rduarte12)
