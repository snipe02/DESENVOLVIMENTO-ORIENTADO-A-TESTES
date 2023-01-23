 """Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!"""


def fatorial(n):
  fatorial = 1
  for c in range(n,0,-1):     # n = start; 0 = stop; -1 = step.
    fatorial *= c
  return fatorial

def resultado(x):
  S = 1
  for c in range(1, x+1):
    S += 1/fatorial(c)
  return S.__round__(3)

while True:
  try:
    numero = int(input('DIGITE NUMERO INTEIRO E POSITIVO '))
    if numero > 0:
      print(f'{resultado(numero)}')
      break
      while numero <= 0:
        numero = int(input())
        if numero > 0:
          print(f'{resultado(numero)}')
          break

  except:
    print('DIGITE VALOR INTEIRO E POSITIVO')