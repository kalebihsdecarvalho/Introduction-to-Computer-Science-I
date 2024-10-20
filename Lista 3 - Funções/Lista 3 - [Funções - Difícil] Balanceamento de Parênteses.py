def balanceamento(lista_string):
  posicao = (len(lista_string) // 2)-1

  if len(lista_string) % 2 != 0:
    return False

  elif lista_string[0] == '(' and lista_string[1] == ')' and len(lista_string) != 2:
    lista_string.pop(0)
    lista_string.pop(0)

    return balanceamento(lista_string)

  elif lista_string[0] == '(' and lista_string[-1] == ')' and len(lista_string) == 2:
    return True

  elif lista_string[0] == lista_string[-1] and len(lista_string) == 2:
    return False

  else:
    if lista_string[posicao] != lista_string[posicao + 1]:
      lista_string.pop(posicao)
      lista_string.pop(posicao)

      return balanceamento(lista_string)

    else:
      return False


    return balanceamento(lista_string)

string = input()
lista = []

for i in range(0, len(string)):
    lista.append(string[i])

print(balanceamento(lista))
