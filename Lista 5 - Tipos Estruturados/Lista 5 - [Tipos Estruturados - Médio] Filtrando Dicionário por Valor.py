def filtro_dicionario(dicionario, valor_lim):
  filtro_dicionario = {}

  for key in dicionario:
    if dicionario[key] > valor_lim:
      filtro_dicionario[key] = dicionario[key]

  return filtro_dicionario

quantidades_pares = int(input())
count = 0
key = 0
value = 0
dicionario_ant = {}

while count < quantidades_pares:
  key = input().replace("\r", "")
  value = int(input().replace("\r", ""))
  dicionario_ant[key] = value
  count += 1

lim = int(input())
print(filtro_dicionario(dicionario_ant, lim))
