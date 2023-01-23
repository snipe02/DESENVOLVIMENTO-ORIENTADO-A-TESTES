"""Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor."""

def somatorio_funcao(a):
    somatorio = 0
    for c in range(1,a+1):
        somatorio += c
        return somatorio

while True:
    try:
        y = int(input())
        if y > 0:
            print(f'{somatorio_funcao(y)}')
            break
        else:
          print("Digite um valor valido ")
          y = int(input())
        if y > 0:
           print(f'{somatorio_funcao(y)}')
           break
        else:
           while type(int)!= type(y):
             y = int(input())
             print(f'{somatorio_funcao(y)}')
             break
    except:
      print('DIGITE UM VALOR VÁLIDO')