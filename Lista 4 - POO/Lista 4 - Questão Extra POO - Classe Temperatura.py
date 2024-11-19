#Crie uma classe chamada Temperatura, que representará uma temperatura em graus Celsius com o atributo celsius. Sua classe deverá conter os seguintes métodos:

#converter_fahrenheit(): Método que converte a temperatura para Fahrenheit usando a fórmula: [ fahrenheit = celsius * 9/5 + 32 ]

#converter_kelvin(): Método que converte a temperatura para Kelvin usando a fórmula: [ kelvin = celsius + 273.15 ]

#O programa deve receber a temperatura em Celsius como entrada e calcular:

#A temperatura em Fahrenheit.
#A temperatura em Kelvin.
#Se a temperatura em Celsius for menor que o zero absoluto (-273.15°C), exiba a mensagem: "A temperatura não pode ser menor que o zero absoluto."

#Caso a temperatura seja válida (não menor que -273.15°C):

#Temperatura em Fahrenheit: valor com uma casa decimal.
#Temperatura em Kelvin: valor com uma casa decimal.

class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def converter_fahrenheit(self):
        fahrenheit = celsius * (9/5) + 32
        return(fahrenheit)

    def converter_kelvin(self):
        kelvin = celsius + 273.15
        return(kelvin)

celsius = float(input())
temp = Temperatura(celsius)

if celsius < -273.15:
    print("A temperatura não pode ser menor que o zero absoluto.")
else:
    print(f'Fahrenheit: {round(temp.converter_fahrenheit(), 1)}\nKelvin: {round(temp.converter_kelvin(), 1)}')