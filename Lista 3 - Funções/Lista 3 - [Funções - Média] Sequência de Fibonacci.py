'Implemente uma função recursiva que retorne o n-ésimo termo da sequência de Fibonacci.'

n = int(input())

def fibonacci(n):
    f_n1,f_n2,f_n = 1,1,0
    
    if 1 <= n <= 2 :
        f_n = f_n1

    elif n >= 3:
        count = n - 2
        while count > 0:
            f_n = f_n1 + f_n2
            f_n1 = f_n2
            f_n2 = f_n
            count -= 1
    return f_n

print(fibonacci(n))
            
            
    
