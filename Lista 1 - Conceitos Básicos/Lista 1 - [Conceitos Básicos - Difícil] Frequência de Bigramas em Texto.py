string = input().lower().split()
contagem_bigramas = {}

for i in range(0, len(string) - 1):
  bigrama = string[i] + ' ' + string[i + 1]
  if bigrama in contagem_bigramas:
    contagem_bigramas[bigrama] += 1
  else:
    contagem_bigramas[bigrama] = 1

for chave, valor in contagem_bigramas.items():
  print(f"{chave}: {valor}")
