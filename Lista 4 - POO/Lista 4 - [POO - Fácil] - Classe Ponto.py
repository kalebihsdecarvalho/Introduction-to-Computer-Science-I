#Implemente uma classe chamada Ponto que deverá representar um ponto no plano cartesiano, com os seguintes atributos:

#x: A coordenada x do ponto.
#y: A coordenada y do ponto.
#A classe deverá conter o seguinte método:
#calculardistancia(outroponto): Método que recebe outro objeto do tipo Ponto e calcula a distância entre o ponto atual e o ponto recebido, usando a fórmula de calcular distância:

#Subtração das coordenadas:

#Subtraímos as coordenadas 𝑥2 e 𝑥1 para encontrar a diferença entre as coordenadas x: (𝑥2 - 𝑥1)
#Subtraímos as coordenadas y2 e y1 para encontrar a diferença entre as coordenadas y: (y2 - y1)
#Elevação ao quadrado:

#Eleve ao quadrado os resultados dessas subtrações para garantir que o valor seja positivo
#Soma dos quadrados:

#Some os resultados dos quadrados
#Raiz quadrada:

#Tire a raiz quadrada da soma para obter a distância final
#O programa deverá receber as coordenadas de dois pontos no plano cartesiano e calcular a distância entre eles.

#Formato de Entrada: Quatro números inteiros, representando as coordenadas dos dois ponto (𝑥1 - y1) e (𝑥2 - y1) nesta ordem

#Formato de Saída: Exiba a distância entre os dois pontos no formato:

#Distância: [valor]

class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def calculardistancia(self,outro):
        distancia = (((self.x - outro.x)**2) + ((self.y - outro.y)**2))**(1/2)
        return(distancia)

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
ponto_1 = Ponto(x_1, y_1)
ponto_2 = Ponto(x_2, y_2)

print(f'Distância: {ponto_1.calculardistancia(ponto_2)}')
