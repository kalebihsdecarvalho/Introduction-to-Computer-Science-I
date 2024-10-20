def unicos(lista):

  lista = list(map(int, lista.split()))
  lista.sort()

  for i in range(0, len(lista) - 1):
    if lista[i] == lista[i + 1]:
      return False
  return True


lista = input()
print(unicos(lista))