"""15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)"""

def valor_s(t):
    s = 0
    for c in range(1, t + 1):
        s += (c ** 2 + 1) / (c + 3)
    return s.__round__(2)

while True:
    try:
        numero = int(input('DIGITE UM VALOR VÁLIDO '))
        if numero > 0:
            print(f'{valor_s(numero)}')
            break
        else:
            numero = int(input())
            print(f'{valor_s(numero)}')
            break

    except:
        print('DIGITE UM VALOR VÁLIDO ')