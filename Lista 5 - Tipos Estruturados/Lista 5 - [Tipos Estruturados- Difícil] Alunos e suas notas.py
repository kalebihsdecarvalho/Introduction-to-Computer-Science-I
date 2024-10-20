def media_nota_alunos(notas_alunos):
  notas_alunos = list(notas_alunos.replace("{", "").replace("}", "").replace("'", "").replace(" ", ""))
  medias = {}

  for i in range(0, len(notas_alunos) - 1):
    if notas_alunos[i] == ']' and notas_alunos[i + 1] == ',':
      notas_alunos[i + 1] = ':'

  notas_alunos = ''.join(notas_alunos).split(":")

  for key in range(0, len(notas_alunos) - 1, 2):
    media_notas_individual = list(map(float, notas_alunos[key + 1].replace("'", "").replace("[", "").replace("]", "").replace(" ", "").split(",")))
    medias[notas_alunos[key]] = round(sum(media_notas_individual) / len(media_notas_individual), 2)
  
  return medias

notas = input()
print(media_nota_alunos(notas))
