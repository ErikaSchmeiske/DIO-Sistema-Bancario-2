# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 20:22:57 2023

@author: Erika
"""

import textwrap

def menu():
    menu = """\n
    
    =============== MENU ==============

    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova Conta
    [lc]\t Listar Contas
    [nu]\t Novo Usuario
    [q]\t Sair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    valor = float(input("Informe o valor do depósito: "))
        
        #Evita depósito de valores negativos
    if valor > 0:
        saldo += valor 
        extrato += f"Deposito:\t R$ {valor: .2f}\n"
        print("\n ======Deposito realizado com sucesso======")
            
    else:
        print("Operação falhou. O valor informado é inválido")
        
        return saldo, extrato

    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
        
        #Verificações
    excedeu_saldo = valor > saldo        
    excedeu_limite = valor > limite        
    excedeu_saques = numero_saques >= LIMITE_SAQUES
     
    if excedeu_saldo:
        print("Você não tem saldo suficiente.")
            
    elif excedeu_limite:
        print("O valor do saque excede o limite.")
        
    elif excedeu_saques:
        print("Você excedeu o limite de saques permitiu.")
        
        #Impedindo o saque de um valor negativo da conta
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t R$ {valor: .2f}\n"
        numero_saques += 1
        print("\n =======Saque realizado com Sucesso!=======")
        
    else:
        print("Operação fahou! O valor informado é inválido.")
    

def exibir_extrato(saldo, extrato):
        print("\n -----------EXTRATO-------------")
        print("Não foram realizadas movimentações." if not extrato else extrato) #IF TERNÁRIO
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("----------------------------------")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF completo: ")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("Já existe um usuário com esse cpf!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento: input("Informe a data de nascimento (dd-mm-aaa): ")
    endereco = input("Informe o endereço completo: ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})  #estrutura de dicionario
    print("=====Usuario Cadastrado com Sucesso=====")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuarios_filtrados else None

    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Inform o CPF do usuario: ")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("\n =======Conta criada com Sucesso!=========")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario não encontrado. Fluxo de criação de conta encerrado.")
    
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia: \t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))

    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor do deposito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
                )
        
        elif opcao == "e":
            exibir_extrato = (saldo, extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break
        
        else:
            print("Opção Inválida. Digite uma opção válida.")

main()