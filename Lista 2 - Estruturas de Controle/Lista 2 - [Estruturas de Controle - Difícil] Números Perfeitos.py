#Desenvolva um programa em Python que encontre e imprima todos os números perfeitos menores ou iguais a um valor N fornecido. Um número perfeito é um número inteiro positivo que é igual à soma de seus divisores próprios (excluindo ele mesmo). Se N for menor que 6, o programa deve exibir uma mensagem de erro: "Erro: valor de N deve ser maior ou igual a 6". Se não houver números perfeitos menores ou iguais a N, o programa deve exibir a mensagem: "Nenhum número perfeito encontrado".

n = int(input())
lista = []
verificacao = []

if n < 6:
    print("Erro: valor de N deve ser maior ou igual a 6")
else:
    for i in range(6, n+1):
        for j in range(1,i):
            if i % j == 0 and i != j:
                verificacao.append(j)
        if sum(verificacao) == i:
            lista.append(i)
            verificacao = []
        else:
            verificacao = []


    if lista == []:
        print("Nenhum número perfeito encontrado")
    else:
        for m in lista:
            print(m, end=" ")
