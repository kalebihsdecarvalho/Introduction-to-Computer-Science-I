def inversao_recursiva(string):
  remocao_string = 0

  if len(string) == 1:
    return string[0]
  else:
    remocao_string = string.pop(-1)
    return remocao_string + inversao_recursiva(string)

string = ' '.join(input()).split()
print(inversao_recursiva(string))
