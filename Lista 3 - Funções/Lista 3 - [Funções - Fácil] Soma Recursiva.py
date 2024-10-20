def soma_rec(n):
  if n == 1:
    return 1
  else:
    return n + soma_rec(n - 1)

n = int(input())
print(soma_rec(n))