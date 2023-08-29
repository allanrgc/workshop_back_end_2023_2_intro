#Classe Conta Bancária Crie uma classe chamada ContaBancaria que tenha 
#atributos como titular, saldo e métodos para depositar e sacar dinheiro.

class Conta:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def __str__(self):
        return f'Titular: {self.titular}\nSaldo: {self.saldo}'

    def depositar(self, saldo):
        deposito = float(input('Quanto deseja depositar? '))
        print('Novo saldo: $',self.saldo + deposito)
    def sacar(self, saldo):
        saque = input('Quanto deseja sacar? ')
        print('Saldo atual: $', self.saldo - saque)
    # def depositar(self):
    #     print('Deposito realizado')
    # def sacar(self):
    #     print('Saque realizado')
        

allan = Conta('Allan', 187980)
print(allan)


allan.depositar(100)