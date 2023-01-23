altura = float(input())
sexo = int(input())

def peso_ideal(altura, sexo):
  if sexo == 1:
    mulher = (62.1*altura) - 44.7
    return mulher.__round__(4)

  elif sexo == 2:
    homem = (72.7*altura) - 58
    return homem.__round__(4)


ch = peso_ideal(altura, sexo)
if sexo == 1 or sexo == 2:
  if sexo == 1:
    mulher = (62.1*altura)-44.7
    print(f'{mulher:.4f}')
  elif sexo == 2:
    homem = (72.7*altura)-58
    print(f'{homem:.4f}')
else:
  print('Digite uma opção válida')