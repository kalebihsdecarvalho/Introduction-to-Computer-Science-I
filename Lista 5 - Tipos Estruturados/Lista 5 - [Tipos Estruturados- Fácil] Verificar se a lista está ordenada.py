def ordenacao(x):

  lista = list(map(int, x.split()))

  for i in range(1, len(lista)):
    if lista[i] < lista[i-1]:
      return False
  return True 

x = input()
print(ordenacao(x))
