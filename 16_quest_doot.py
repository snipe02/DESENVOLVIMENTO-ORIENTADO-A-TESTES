"""16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
Escrever as listas X e Y."""

from random import randint
listaX =[]
listaY=[]
listaY_nova =[]
for c in range(10):
    num = randint(1,100)
    listaX.append(num)


for d in range(10):
    numero = randint(1,100)
    listaY.append(numero)


for i, v in enumerate(listaY):
    if i % 2 == 0:
        listaY_nova.append(listaX[i]/2)
    else:
        listaY_nova.append(listaX[i]*3)

print(listaX)
print(listaY)
print(listaY_nova)








