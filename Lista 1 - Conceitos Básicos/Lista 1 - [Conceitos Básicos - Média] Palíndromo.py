string = input().lower()
string = ''.join(string.split())
string_invertida = string[::-1]

if string == string_invertida:
  print("Sim")
else:
  print("Não")
