#Implemente uma classe chamada Triangulo com os seguintes atributos:

#lado1: Comprimento do primeiro lado.
#lado2: Comprimento do segundo lado.
#lado3: Comprimento do terceiro lado.
#A classe deverá conter os seguintes métodos:

#verificar_validez(): Verifica se os três lados formam um triângulo válido, ou seja, se a soma de dois lados é sempre maior que o terceiro.
#calcular_perimetro(): Retorna o perímetro do triângulo, que é a soma dos três lados.
#calcular_area(): Calcula e retorna a área do triângulo usando a fórmula simplificada abaixo.
#Cálculo da área:

#Primeiro, calcule o semi-perímetro 𝑠, que é a soma dos três lados dividida por 2: 𝑠 =(𝑙𝑎𝑑𝑜1 + 𝑙𝑎𝑑𝑜2+ 𝑙𝑎𝑑𝑜3)/2.Em seguida, a área do triângulo é calculada da seguinte forma: 𝐴 =(𝑠⋅(𝑠−𝑙𝑎𝑑𝑜1)⋅(𝑠−𝑙𝑎𝑑𝑜2)⋅(𝑠−𝑙𝑎𝑑𝑜3))^0.5

#O uso do ^0.5 representa a raiz quadrada de toda a expressão.

#O programa deverá receber os valores dos três lados do triângulo e, se os lados formarem um triângulo válido, deverá exibir:

#Que o triângulo é válido.
#O perímetro do triângulo.
#A área do triângulo.
#Se os lados não formarem um triângulo válido, o programa deverá exibir uma mensagem indicando que o triângulo é inválido.

#Formato de Entrada:

#Três números representando os lados do triângulo.
#Formato de Saída:

#Se o triângulo for válido, exiba:
#Triângulo válido Perímetro: [valor] Área: [valor]

#Caso contrário, exiba:

#Triângulo inválido

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def verificar_validez(self):
        verificar = True 
        if self.lado1 + self.lado2 <= self.lado3:
            return f'Triângulo inválido'
        if self.lado2 + self.lado3 <= self.lado1:
            return f'Triângulo inválido'
        if self.lado1 + self.lado3 <= self.lado2:
            return f'Triângulo inválido'
        else:
            return f'Triângulo válido'
    
    def calcular_perimetro(self):
        return(self.lado1 + self.lado2 + self.lado3)
    
    def calcular_area(self):
        s = (self.lado1 + self.lado2 + self.lado3)/2
        return((s*(s - self.lado1)*(s - self.lado2)*(s - self.lado3))**0.5)


lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

triangulo = Triangulo(lado1, lado2, lado3)

if triangulo.verificar_validez() != 'Triângulo inválido':
    print(f'{triangulo.verificar_validez()}\n'
          f'Perímetro: {triangulo.calcular_perimetro()}\n'
          f'Área: {triangulo.calcular_area()}')
else:
    print(triangulo.verificar_validez())

    