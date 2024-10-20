string = input().lower().split()
ocorrencias = {}

for i in string:
  if i in ocorrencias:
    ocorrencias[i] += 1
  else:
    ocorrencias[i] = 1

for chave, valor in ocorrencias.items():
  print(f"{chave}: {valor}")