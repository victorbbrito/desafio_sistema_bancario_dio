from cliente import Cliente
from datetime import datetime

class Conta():
    def __init__(self):
      self.cliente:Cliente
      self.agencia = None
      self.conta = None
      self.saldo = 0
      self.extrato = []
    
    def __str__(self) -> str:
       return f"Agencia: {self.agencia}\nConta: {self.conta}\nNome: {self.cliente.nome}\nCPF: {self.cliente.cpf}\nSaldo: {self.saldo}"

    def __repr__(self) -> str:
        return f"Conta <{self.agencia}|{self.conta}>"

    def depositar(self, valor:int):
        if valor > 0:
            self.extrato.append([valor,datetime.now()])
            self.saldo += valor
        else:
            print("Valor deve ser maior que zero!")
    
    def sacar(self, valor:int):
        
        saques_diarios = 0
        
        for i in self.extrato:
            
            if i[0] < 0 and i[1].date().day == datetime.now().date().day:
                
                saques_diarios += 1
        
        if self.saldo - valor >= 0:
            
            if saques_diarios < 3:
                
                if valor <= 500:
                    
                    self.extrato.append([-valor,datetime.now()])
                    
                    self.saldo -= valor
                
                else:
                    
                    print(f"sacar({valor}) => Erro:\nValor maior que R$ 500,00.")
            
            else:
                
                print(f"sacar({valor}) => Erro:\nLimite de saques diários atingido.")
        else:
                
            print(f"sacar({valor}) => Erro:\nSaldo insuficiente.")
    
    def ver_extrato(self):
                
        print("------------------EXTRATO------------------")
        print(f"SALDO:{self.saldo}\n")
        for i in self.extrato:
            if i[0] > 0:
                print(f"Depósito => +{i[0]} -- {i[1].strftime(r'%d-%m-%Y | %H:%M:%S')} ")
            else:
                print(f"Saque => {i[0]} -- {i[1].strftime(r'%d-%m-%Y | %H:%M:%S')} ")
                
        print(f'----------{datetime.now().strftime(r" %d-%m-%Y | %H:%M:%S ")}----------')
    
    def criar_cliente(self, cliente:Cliente):
        self.cliente = cliente
            
    def criar_conta(self, agencia, conta):
        self.agencia = agencia
        self.conta = conta
    
def procurar_conta_do_cliente(lista:list, key) -> Conta:
    for conta in lista:
        if key in conta.cliente.nome:
            return conta
        elif key in conta.cliente.cpf:
            return conta
        
    return None

def entrar_na_conta(lista:list, agencia, n_conta) -> Conta:
    for item in lista:
        if item.agencia == agencia and item.conta == n_conta:
            return item
    
    return None

                
            
    