

def funcao_funk(fatorial):
    fatorial_funk = 1

    for c in range(fatorial, 1,  -1):
        fatorial_funk *= c
        return fatorial_funk

while True:
  try:
    funcao = int(input())
    cha = fatorial_funk(faltorial)
    print(cha)
    break

  except:
    print('valor invalido, entre com un número inteiro')