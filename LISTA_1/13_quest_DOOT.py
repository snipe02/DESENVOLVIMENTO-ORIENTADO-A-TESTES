"""Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N."""

def valor(y):
    S = 1
    for c in range(2, y+1):
        S += 1/c
    return S.__round__(3)



while True:
    try:
        numero = int(input())
        if numero > 0:
            print(f'{valor(numero)}')
            break

        else:
            print('ESTE VALOR NÃO É ACEITO. DIGITE UM NÚMERO INTEIRO E POSITIVO')

    except:
        print('ESTE VALOR NÃO É ACEITO. DIGITE UM NÚMERO INTEIRO E POSITIVO')


