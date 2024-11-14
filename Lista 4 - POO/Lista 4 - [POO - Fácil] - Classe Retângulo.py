#Crie uma classe chamada Retangulo que representará um retângulo com dois atributos: largura e altura. Sua classe deverá conter os seguintes métodos:

#calcular_area(): Método que retorna a área do retângulo.
#calcular_perimetro(): Método que retorna o perímetro do retângulo.
#O programa deve receber as dimensões (largura e altura) do retângulo como entrada e calcular:

#A área: largura * altura.
#O perímetro: 2 * (largura + altura).
#O resultado deve ser impresso no seguinte formato:

#Área: valor da área com uma casa decimal.
#Perímetro: valor do perímetro com uma casa decimal.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return(round(self.largura*self.altura, 2))

    def calcular_perimetro(self):
        return(round(2*(self.largura + self.altura), 2))
    
largura = float(input())
altura = float(input())

dimensoes = Retangulo(largura, altura)
print(f'Área: {dimensoes.calcular_area()}')
print(f'Perímetro: {dimensoes.calcular_perimetro()}')
        
