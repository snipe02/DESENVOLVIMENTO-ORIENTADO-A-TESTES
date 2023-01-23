""" Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor."""

def numero_divisores(a):
    divisores = 0
    for s in ranger(1, a+1):
        if a% s == 0:
            divisores += 1

    return divisores

while True:
    try:
        numero = int(input("Digite o valor 1 "))
        if numero > 0:
          chama = numero_divisores(numero)
          print(chama)
          break
          while numero != type(int):
            print("Digite um valor invalido 2 ")
            numero  = int(input("Digite o valor valido 3"))
            chama = numero_divisores(numero)
            print(chama)
            break
    except:
        print("Digite um invalido 4")




