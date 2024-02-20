from conta import Conta
from conta import procurar_conta_do_cliente
from conta import entrar_na_conta
from cliente import Cliente

if __name__ == '__main__':
    
    lista_contas = []
    
    menu = """
Digite uma opção:
n - Novo Cliente
c - Nova Conta
d - Depósito
s - Saque
e - Extrato
v - Lista de Contas
q - Sair

"""
    
    while True:
        
        opcao = input(menu)
        
        if opcao == 'n':
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            novo_cliente = Cliente(nome, cpf)
            nova_conta = Conta()
            nova_conta.criar_cliente(novo_cliente)
            lista_contas.append(nova_conta)
        
        elif opcao == 'c':
            nome = input("Nome do cliente: ")
            conta = procurar_conta_do_cliente(lista_contas, nome)
            if conta == None:
                cpf = input("CPF do cliente: ")
                agencia = input("Agencia: ")
                n_conta = input("Conta: ")
                
                novo_cliente = Cliente(nome, cpf)
                nova_conta = Conta()
                nova_conta.criar_cliente(novo_cliente)
                nova_conta.criar_conta(agencia, n_conta)
                lista_contas.append(nova_conta)
            else:
                agencia = input("Agencia: ")
                n_conta = input("Conta: ")
                conta.criar_conta(agencia,n_conta)
        
        elif opcao == "d":
            agencia = input("Agencia: ")
            n_conta = input("Conta: ")
            conta = entrar_na_conta(lista_contas,agencia, n_conta)
            
            if conta != None:
                conta.depositar(int(input("Valor do depósito: ")))
                print(f"Saldo: {conta.saldo}")
            else:
                print("Conta não encontrada.")
        
        elif opcao == "s":
            agencia = input("Agencia: ")
            n_conta = input("Conta: ")
            conta = entrar_na_conta(lista_contas,agencia, n_conta)
            
            if conta != None:
                conta.sacar(int(input("Valor do saque: ")))
                print(f"Saldo: {conta.saldo}")
                
            else:
                print("Conta não encontrada.")
                
        elif opcao == 'e':
            agencia = input("Agencia: ")
            n_conta = input("Conta: ")
            
            conta = entrar_na_conta(lista_contas,agencia, n_conta)
            
            if conta != None:
                conta.ver_extrato()
                
            else:
                print("Conta não encontrada.")
        
        elif opcao == 'v':
            print(lista_contas)
        
        elif opcao == "q":
        
            break
            
        else:
            
            print("Opção inválida, por favor selecione novamente a operação desejada.")