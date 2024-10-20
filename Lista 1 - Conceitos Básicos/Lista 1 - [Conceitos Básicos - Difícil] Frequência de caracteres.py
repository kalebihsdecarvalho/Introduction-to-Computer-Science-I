string = input().lower()
string = ' '.join(string).split()
frequencia = {}

for letra in string:
  if letra in frequencia:
    frequencia[letra] += 1
  else:
    frequencia[letra] = 1

for chave, valor in frequencia.items():
  print(f"{chave}: {valor}")
