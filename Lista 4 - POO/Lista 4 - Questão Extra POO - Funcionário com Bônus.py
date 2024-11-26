#Crie uma classe chamada Funcionario, que representará um funcionário com os atributos nome, salario e percentual_bonus. Sua classe deverá conter os seguintes métodos:

#calcularbonus(): Método que calcula o valor do bônus com base no salário e no percentual de bônus. A fórmula é: [ bonus = salario * percentualbonus/100 ]

#calcularsalariocom_bonus(): Método que retorna o salário total do funcionário somado ao bônus.

#exibir_detalhes(): Método que exibe os detalhes do funcionário no formato: "Funcionário: <nome>, Salário Base: R$ <salario>, Bônus: R$ <bonus>, Salário Total: R$ <salario_total>".

#O programa deve receber o nome, o salário base e o percentual de bônus do funcionário e calcular:

#O valor do bônus.
#O salário total com o bônus.
#Os detalhes formatados como especificado.
#Se o salário ou o percentual de bônus forem negativos, exiba a mensagem: "O salário e o percentual de bônus devem ser números positivos."

#Caso os valores sejam válidos:

#Exiba o nome do funcionário, o salário base, o bônus e o salário total, todos formatados com duas casas decimais.

class Funcionario:
    def __init__(self, nome, salario, percentual_bonus):
        self.nome = nome
        self.salario = salario
        self.percentual_bonus = percentual_bonus

    def calcular_bonus(self):
        return self.salario * self.percentual_bonus / 100

    def calcular_salario_com_bonus(self):
        return self.salario + self.calcular_bonus()

    def exibir_detalhes(self):
        bonus = self.calcular_bonus()
        salario_total = self.calcular_salario_com_bonus()
        return (f'Funcionário: {self.nome}, Salário Base: R$ {self.salario:.2f}, '
                f'Bônus: R$ {bonus:.2f}, Salário Total: R$ {salario_total:.2f}')


nome = input().strip()
salario_base = float(input())
percentual_bonus = float(input())

if salario_base < 0 or percentual_bonus < 0:
    print('O salário e o percentual de bônus devem ser números positivos.')
else:
    funcionario = Funcionario(nome, salario_base, percentual_bonus)
    print(funcionario.exibir_detalhes())

    
