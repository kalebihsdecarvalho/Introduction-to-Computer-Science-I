min, max = map(int, input().split(','))
lista = []

for i in range(min, max + 1):
  if i % 5 == 0 and i % 7 == 0:
    lista.append(str(i))

num = ','.join(lista)
print(num)