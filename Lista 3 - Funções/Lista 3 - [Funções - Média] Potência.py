#Implemente uma função recursiva que calcule a potência de um número inteiro base elevado a um expoente exp.

def potencia(base, exp):
  #Caso Base 
  if exp == 0:
    return 1
  #Caso Recursivo
  elif exp > 0:
    return base * potencia(base, exp - 1)
  else:
    return potencia(1/base, -exp) 

x,y = map(int, input().split())
print(potencia(x, y))
