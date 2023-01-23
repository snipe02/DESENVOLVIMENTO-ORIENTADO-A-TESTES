"""Prova1_q3. Faça uma função para ler/gravar uma lista X de 10 elementos inteiros
e positivos. Criar uma lista Y da seguinte forma: os elementos de Y com índice
par receberão os respectivos elementos de X divididos por 2; os elementos com
índice ímpar receberão os respectivos elementos de X multiplicados por 3.
Obs: Usar uma função para gravar a lista X e outra para gerar a lista Y.
Exemplo: X [4,5,2,7,10,1,8,0,12,11]
         Y [2,15,1,21,5,3,4,0,6,33]"""

from random import randint

listaX = []

def add():
    for c in range(3):
        adc = randint(2,15)
        listaX.append(adc)

listaY = list()
def loadY(listaX):
    for ind, val in enumerate(listaX):
        if ind%2 == 0:
            listaY.append(listaX[ind]/2)
        else:
            listaY.append(listaX[ind]*3)

ch1 = loadY(listaX)

print(listaY)





