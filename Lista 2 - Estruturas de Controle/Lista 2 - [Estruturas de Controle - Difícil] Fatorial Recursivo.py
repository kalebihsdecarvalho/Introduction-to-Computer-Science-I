def fato_rec(n):
  if n < 0:
    return print("Erro: número negativo")
  elif n == 0 or n == 1:
    return 1
  else:
    return n * fato_rec(n - 1)

n = int(input())
print(fato_rec(n))