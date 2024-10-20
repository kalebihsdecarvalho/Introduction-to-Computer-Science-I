horas, minutos, segundos = map(int, input().split(':'))

conversao = segundos + (minutos * 60) + (horas * 60**2)
print(conversao)