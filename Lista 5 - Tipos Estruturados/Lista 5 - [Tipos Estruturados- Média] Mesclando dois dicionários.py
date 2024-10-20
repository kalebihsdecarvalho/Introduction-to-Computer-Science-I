def meslcar_dicionarios(x, y):
  x, y = x.replace("'", "").replace("{", "").replace("}", "").replace(" ", ""), y.replace("'", "").replace("{", "").replace("}", "").replace(" ", "")
  x, y = ' '.join(x).split(), ' '.join(y).split()
  mesclado = {}

  for elemento_x in range(0, len(x)):
    if x[elemento_x] == ',':
      x[elemento_x] = ':'

  x = ''.join(x).split(':')

  for elemento_y in range(0, len(y)):
    if y[elemento_y] == ',':
      y[elemento_y] = ':'
  
  y = ''.join(y).split(':')

  for i in range(0, len(x) - 1, 2):
    mesclado[x[i]] = int(x[i + 1])

  for j in range(0, len(y) - 1, 2):
    if y[j] in mesclado:
      if x[j + 1] >= y[j + 1]:
        mesclado[y[j]] = int(x[j + 1])
      else:
        mesclado[y[j]] = int(y[j + 1])
    else:
      mesclado[y[j]] = int(y[j + 1])
  
  return mesclado

dicio_x, dicio_y = input().split(";")
print(meslcar_dicionarios(dicio_x, dicio_y))
