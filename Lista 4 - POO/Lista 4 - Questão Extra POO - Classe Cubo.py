#Crie uma classe chamada Cubo, que representará um cubo com o atributo aresta. Sua classe deverá conter os seguintes métodos:

#calcular_volume(): Método que retorna o volume do cubo.
#calcular_areasuperficie(): Método que retorna a área da superfície do cubo.
#Se a medida da aresta for negativa, exiba a mensagem: "A aresta deve ser um número positivo."

#O programa deve receber a medida da aresta do cubo como entrada e calcular:

#O volume: ( aresta^3 ).
#A área da superfície: ( 6 * aresta^2 ).
#O resultado deve ser impresso no seguinte formato:

#Volume: valor do volume com uma casa decimal.
#Área da Superfície: valor da área com uma casa decimal.

class Cubo:
    def __init__(self, aresta):
        self.aresta = aresta

    def calcular_volume(self):
        return(self.aresta**3)

    def calcular_areasuperficie(self):
        return(6*(self.aresta**2))

aresta = float(input())
medida = Cubo(aresta)

if aresta < 0:
    print('A aresta deve ser um número positivo.')
else:
    print(f'Volume: {round(medida.calcular_volume(), 1)}\nÁrea da Superfície: {round(medida.calcular_areasuperficie(), 1)}')


    
