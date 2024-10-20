def mdc_recursivo(a, b):
  if b == 0:
    return a
  else:
    return mdc_recursivo(b, a % b)

num = list(map(int, input().split()))
num.sort()
print(mdc_recursivo(num[1], num[0]))
