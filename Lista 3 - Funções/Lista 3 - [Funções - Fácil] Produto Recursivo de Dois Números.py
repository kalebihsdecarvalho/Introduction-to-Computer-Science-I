def produto_rec(a, b):
  if a == 0 or b == 0:
      return 0
  elif b == 1:
    return a
  else:
    return a + produto_rec(a, b - 1)

a, b = map(int, input().split())
print(produto_rec(a, b))