menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta Corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = {}
conta_corrente = {}
num_conta_inicial = 0

def deposito(saldo, extrato, /):
	valor = float(input("Informe o valor do depósito: "))

	if valor > 0:
		saldo += valor
		extrato += f"Depósitos: R$ {valor:.2f}\n"
		return saldo, extrato
	
	else:
		print("Operaçao falhou! O valor informado é inválido.")
	
def saque(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
	valor = float(input("Informe o valor do saque: "))

	excedeu_saldo = valor > saldo
	excedeu_limite = valor > limite
	excedeu_saques = numero_saques >= LIMITE_SAQUES

	if excedeu_saldo:
		print("Operação falhou! Você não tem saldo suficiente.")
	elif excedeu_limite:
		print("Operação falhou! O valor do saque excede o limite.")
	elif excedeu_saques:
		print("Operação falhou! Número máximo de saques excedidos.")
	elif valor > 0:
		saldo -= valor
		extrato += f"Saque: R$ {valor:.2f}\n"
		numero_saques += 1
		return saldo, extrato
	else:
		print("Operação falhou! O valor informado é inválido.") 
	
def tirar_extrato(saldo, /, *, extrato):
	print("\n================ EXTRATO ================")
	print("Não foram realizadas movimentações." if not extrato else extrato)
	print(f"\nSaldo: R$ {saldo:.2f}")
	print("==========================================")

def criar_usuario():
	cpf = input("Digite o CPF: ")

	verificacao_cpf = len(cpf) == 11 
	verificacao_cpf_existe = usuarios.get(cpf)

	if verificacao_cpf_existe:
		print('[ERRO] CPF já existe')
	elif verificacao_cpf:
		nome = input("Digite seu nome: ")
		data_nasc = input("Digite a data do seu nascimento: ")
		endereco = input("Digite seu endereço: ")

		usuario = {
			cpf: {
				"nome": nome,
				"data_nasc": data_nasc,
				"endereço": endereco
			}
		}
		
		usuarios.update(usuario)	
	else:
		print("\n[ERRO] CPF Inválido.")

def criar_conta_corrente(num_conta):

	cpf = input("Digite o CPF: ")
	validacao_cpf = usuarios.get(cpf)
	
	if validacao_cpf == None:
		print("Esse CPF não está cadastrado")
		return 0
	else:
		nome_usuario = usuarios[cpf]["nome"]
		agencia_padrao = "0001"
		num_conta += 1

		conta = {
			nome_usuario: {
				"agência": agencia_padrao,
				"número_conta": f'{num_conta:02}',
				"usuário": cpf
			}
		}

		conta_corrente.update(conta)
		return num_conta
	

while True:

	opcao = input(menu)

	if opcao == "d":
		tuplaDeposito = deposito(saldo, extrato)
		if tuplaDeposito != None:
			saldo = tuplaDeposito[0]
			extrato = tuplaDeposito[1]
	elif opcao == "s":
		tuplaSaque = saque(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
		if tuplaSaque != None:
			saldo = tuplaSaque[0]
			extrato = tuplaSaque[1]
	elif opcao == "e":
		tirar_extrato(saldo, extrato=extrato)
	elif opcao == "u":
		criar_usuario()
	elif opcao == "c":
		num_conta_inicial = criar_conta_corrente(num_conta_inicial)
	elif opcao == "q":
		break
	else:
		print("Operação inválida, por favor selecione novamente a operação desejada.")
	
	for chave, valor in conta_corrente.items():
		print("Contas corrente: ", chave, valor)

	for chave, valor in usuarios.items():
		print("Usuários criados: ", chave, valor)

	
		