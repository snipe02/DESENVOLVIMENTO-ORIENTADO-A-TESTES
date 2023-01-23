def max(a,b,c,d):
  maior = a
  if b > maior:
      maior = b
  if c > maior:
      maior = c
  if d > maior:
    maior = d
    return maior

for i in range(4):
  print("%d serio de 4 numero ***** "% (i + 1))
  num1 = int(input("Digite o primeiro numero: "))
  num2 = int(input("Digite o segundo numero: "))
  num3 = int(input("Digte o terceiro numero: "))
  num4 = int(input("Digite o quarto numero: "))
  print("===> o maior é ",max (num1,num2,num3,num4))