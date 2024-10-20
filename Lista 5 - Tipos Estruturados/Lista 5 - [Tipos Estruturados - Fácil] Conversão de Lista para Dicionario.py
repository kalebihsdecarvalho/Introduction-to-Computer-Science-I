def conversao_dicionario(lista_tuplas):
  dicionario_conversao = {}

  for i in range(0, len(lista_tuplas)):
    dicionario_conversao[lista_tuplas[i][0]] = lista_tuplas[i][1]
  
  return dicionario_conversao

contador_tuplas = int(input())
count = 0
key, value = 0, 0
tupla = ()
lista_tuplas = []


while count < contador_tuplas:
  key = input().replace("\r", "")
  value = input().replace("\r", "")
  tuplas = (key, value)
  lista_tuplas.append(tuplas)
  count += 1

print(conversao_dicionario(lista_tuplas))
