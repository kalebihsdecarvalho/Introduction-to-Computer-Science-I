#Desenvolva um código em Python que leia uma lista de números inteiros e escreva a lista em ordem crescente.

entrada = list(map(int, input().split()))
entrada.sort()

for i in entrada:
    print(i, end=" ")
