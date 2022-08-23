altura = float(input())
sexo = int(input())

def peso_ideal(a, b):
    if b == 1:
        mulher = (62.1*a)-44.7
        return mulher

    elif b == 2:
         homem = (72.7*a)-58
         return homem

cha = peso_ideal(altura,sexo)

print(cha)
