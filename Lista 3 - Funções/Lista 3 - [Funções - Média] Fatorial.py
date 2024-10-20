def fatorial_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fatorial_rec(n - 1)

n = int(input())
print(fatorial_rec(n))