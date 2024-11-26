#Implemente uma classe chamada Funcionario com os seguintes atributos:

#nome: O nome do funcionário.
#salario: O salário base do funcionário.
#Em seguida, crie uma classe Gerente que herda de Funcionario e adiciona o atributo:

#departamento: O departamento no qual o gerente trabalha.
#Ambas as classes devem ter um método chamado calcular_bonus():

#Para Funcionario, o bônus será de 10% do salário base.
#Para Gerente, o bônus será de 20% do salário base.
#O programa deverá solicitar ao usuário as informações de um funcionário (nome e salário) e de um gerente (nome, salário e departamento). Em seguida, deverá calcular e exibir o salário com bônus de ambos.

#Formato de Entrada:

#Nome do funcionário.
#Salário do funcionário.
#Nome do gerente.
#Salário do gerente.
#Departamento do gerente.
#Formato de Saída: O nome do funcionário e o seu salário com bônus no formato:

#Nome: Salário com bônus = [valor]
#O nome do gerente e o seu salário com bônus no formato:

#Nome: Salário com bônus = [valor]

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
         return (self.salario * 10 / 100) + self.salario
        
    def exibir_detalhes(self):
        return(f'{self.nome}: Salário com bônus = {self.calcular_bonus()}')
        

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return (self.salario * 20 / 100) + self.salario

    def exibir_detalhes(self):
        detalhes_basicos = super().exibir_detalhes()
        return(f'{detalhes_basicos}')

nome_funcionario = input().strip()
salario_funcionario = float(input())
nome_gerente = input().strip()
salario_gerente = float(input())
departamento_gerente = input().strip()

funcionario = Funcionario(nome_funcionario, salario_funcionario)
gerente = Gerente(nome_gerente, salario_gerente, departamento_gerente)

print(f'{funcionario.exibir_detalhes()}\n'
      f'{gerente.exibir_detalhes()}')
    

        
        
