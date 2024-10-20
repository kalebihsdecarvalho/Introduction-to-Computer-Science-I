def lista_tuplas(entrada):
  lista_tuplas = []

  entrada = entrada.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "").split(", ")

  for i in range(0, len(entrada), 2):
    nome = entrada[i]
    idade = int(entrada[i + 1])
    tuplas = (nome, idade)
    lista_tuplas.append(tuplas)

  ordenacao = sorted(lista_tuplas, key=lambda x: x[1])
  return ordenacao

entrada = input()
print(lista_tuplas(entrada))
