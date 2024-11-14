#Implemente uma classe chamada ContaBancaria que deverá possuir os seguintes atributos:

#titular: O nome do titular da conta bancária.
#saldo: O saldo inicial da conta.
#A classe deve conter os seguintes métodos:

#depositar(valor): Método para adicionar o valor informado ao saldo da conta.
#sacar(valor): Método para subtrair o valor informado do saldo da conta, garantindo que o saldo nunca fique negativo. Se o valor do saque for maior que o saldo disponível, o saque não será realizado e o saldo permanecerá o mesmo.
#O programa deverá receber como entrada:

#O nome do titular da conta.
#O saldo inicial da conta.
#O valor de um depósito.
#O valor de um saque.
#Após processar as operações, o programa deverá exibir o saldo final da conta.

#Formato de Entrada:

#Nome do titular.
#Saldo inicial da conta.
#Valor do depósito.
#Valor do saque.
#Formato de Saída: Exiba o saldo final da conta com uma casa decimal.

class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor
        return(self.saldo)

    def sacar(self,valor):
        self.saldo -= valor
        return(self.saldo)

titular = input()
saldo = float(input())
deposito = float(input())
saque = float(input())

info = ContaBancaria(titular,saldo)
info_saldo = info.depositar(deposito)
info_saldo = round(info.sacar(saque),1)

print(f'Saldo final: {info_saldo}')

