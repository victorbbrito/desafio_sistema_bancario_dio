from datetime import datetime

saldo = 0

depositos = []
saques = []

def depositar(valor:int):
    if valor > 0:
        depositos.append([valor,datetime.now()])
        global saldo
        saldo += valor
    else:
        print("Valor deve ser maior que zero!")
        
def sacar(valor:int):
    saques_diarios = 0
    for i in saques:
        i[1].date().day == datetime.now().date().day
        saques_diarios += 1
    global saldo
    
    if saldo - valor >= 0:
        
        if saques_diarios < 3:
            
            if valor <= 500:
                
                saques.append([-valor,datetime.now()])
                
                saldo -= valor
            
            else:
                
                print(f"sacar({valor}) => Erro:\nValor maior que R$ 500,00.")
        
        else:
            
            print(f"sacar({valor}) => Erro:\nLimite de saques diários atingido.")
    else:
            
        print(f"sacar({valor}) => Erro:\nSaldo insuficiente.")

def extrato():
    extrato = saques + depositos
    global saldo
    
    print("------------------EXTRATO------------------")
    print(f"SALDO:{saldo}\n")
    for i in extrato:
        if i[0] > 0:
            print(f"Depósito => +{i[0]} -- {i[1].strftime(r'%d-%m-%Y | %H:%M:%S')} ")
        else:
            print(f"Saque => {i[0]} -- {i[1].strftime(r'%d-%m-%Y | %H:%M:%S')} ")
            
    print(f'----------{datetime.now().strftime(r" %d-%m-%Y | %H:%M:%S ")}----------')

if __name__ == '__main__':
    menu = """
Digite uma opção:
d - Depósito
s - Saque
e - Extrato
q - Sair

"""
    
    while True:
        
        opcao = input(menu)
        
        if opcao == "d":
        
            depositar(int(input("Valor do depósito: ")))
        
        elif opcao == "s":
        
            sacar(int(input("Valor do saque: ")))
        
        elif opcao == 'e':
        
            extrato()
        
        elif opcao == "q":
        
            break
            
        else:
            
            print("Opção inválida, por favor selecione novamente a operação desejada.")