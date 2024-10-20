def letras(string):
  maiuscula = 0
  minuscula = 0
  count = 0

  while count < len(string):
    if string[count].isalpha() == False:
      string.pop(count)
      count = 0
    else:
      count += 1

  for i in string:
    if i == i.lower():
      minuscula += 1
    else:
      maiuscula += 1

  tupla = (maiuscula, minuscula)

  return tupla

string = ' '.join(input().replace(" ", "")).split()
print(f'Maiúsculas: {letras(string)[0]}\nMinúsculas: {letras(string)[1]}')
