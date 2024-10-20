def mesclar_dicionarios(primeiro_dicio, segundo_dicio):
  mesclado = {}

  for key_pri in primeiro_dicio:
    mesclado[key_pri] = primeiro_dicio[key_pri]

  for seg_key in segundo_dicio:
    if seg_key in primeiro_dicio:
      mesclado[seg_key] = primeiro_dicio[seg_key] + segundo_dicio[seg_key]
    else:
      mesclado[seg_key] = segundo_dicio[seg_key]

  return mesclado

num_chaves =  int(input())
count = 0
primeiro = {}
segundo = {}
key = 0
value = 0 

while count < num_chaves:
  key = input().replace("\r", "")
  value = int(input())
  primeiro[key] = value
  count += 1

count = 0
num_chaves = int(input())

while count < num_chaves:
    key = input().replace("\r", "")
    value = int(input())
    segundo[key] = value
    count += 1

print(mesclar_dicionarios(primeiro, segundo))
