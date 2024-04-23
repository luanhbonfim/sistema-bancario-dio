import os

extrato_deposito = []
extrato_saque = []
saldo_conta = 0
limite_saque = 0

RETURN_ZERO = 0

RESPOSTA_ERRO = "[INVÁLIDO] Não foi possível completar a operação."
RESPOSTA_SEM_SALDO = "[INVÁLIDO] Você está sem saldo."
RESPOSTA_OPCAO = "Seleciona uma opção: \n  -> "
RESPOSTA_SALDO_ATUAL = "\n -> Seu saldo atual é: "

def saque():
    valor_saque = int(input("Digite o valor para sacar: "))

    CONDICAO_SEM_SALDO = saldo_conta <= 0

    if CONDICAO_SEM_SALDO:
        print(RESPOSTA_SEM_SALDO)
        return RETURN_ZERO
    
    CONDICAO_SAQUE = limite_saque <= 3 and valor_saque <= 500

    if CONDICAO_SAQUE:
        extrato_saque.append(f"Valor R$ {valor_saque:.2f}")
        print(f"\n[SUCESSO] Você sacou R$ {valor_saque:.2f}")
        return valor_saque
    else:
        print(RESPOSTA_ERRO)
        return RETURN_ZERO


def deposito():
    valor_deposito = int(input("Digite o valor do deposito: "))

    CONDICAO_DEPOSITO = valor_deposito > 0

    if CONDICAO_DEPOSITO:
        extrato_deposito.append(f"Valor R$ {valor_deposito:.2f}")
        print(f"\n[SUCESSO] Você depositou R$ {valor_deposito:.2f}")
        return valor_deposito
    else: 
        print(RESPOSTA_ERRO)
        return 0


def extrato():
    print(f"""
    # - - - - - EXTRATO - - - - - 
    # [1] - Depositos           #
    # [2] - Saques              #    
    # # # # # # # # # # # # # # # 
    """)
    opcao_extrato = int(input(RESPOSTA_OPCAO))

    if opcao_extrato == 1:
        print("EXTRATO DE DEPOSITOS".center(10, "#"))
        for deposito in extrato_deposito:
            print("->", deposito)
    elif opcao_extrato == 2:
        print("EXTRATO DE SAQUES".center(10, "#"))
        for saque in extrato_saque:
            print("->", saque)
    else:
        print(RESPOSTA_ERRO)

os.system('cls')
opcao_iniciar_sistema = str(input("Deseja iniciar o sistema? (SIM/NÃO)\n  -> ")).upper()

while opcao_iniciar_sistema == "SIM":

    print(f"""
    # - - - - - SYSTEM BANCÁRIO - - - - - 
    # [1] - Depositos                   #
    # [2] - Saques                      #
    # [3] - Extratos                    #
    # # # # # # # # # # # # # # # # # # #
    """)
    opcaoMenu = int(input(RESPOSTA_OPCAO ))

    if opcaoMenu == 1:
        saldo_conta += deposito()
        print(f'{RESPOSTA_SALDO_ATUAL} R$ {saldo_conta:.2f}')
    elif opcaoMenu == 2:
        limite_saque += 1
        saldo_conta -= saque()
        print(f'{RESPOSTA_SALDO_ATUAL} R$ {saldo_conta:.2f}')
    elif opcaoMenu == 3:
        os.system('cls')
        extrato()
        print(f'{RESPOSTA_SALDO_ATUAL} R$ {saldo_conta:.2f}')
    else:
        print(RESPOSTA_ERRO)

    opcao_iniciar_sistema = str(input("\n\nSe deseja continuar com as operações digite SIM:\n  -> ")).upper()
    os.system('cls')

else:
    print('Fechando sistema....')


    




