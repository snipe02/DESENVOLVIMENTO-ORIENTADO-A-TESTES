"""Prova1_q3. Faça uma função para ler/gravar uma lista X de 10 elementos inteiros
e positivos. Criar uma lista Y da seguinte forma: os elementos de Y com índice
par receberão os respectivos elementos de X divididos por 2; os elementos com
índice ímpar receberão os respectivos elementos de X multiplicados por 3.
Obs: Usar uma função para gravar a lista X e outra para gerar a lista Y.
Exemplo: X [4,5,2,7,10,1,8,0,12,11]
         Y [2,15,1,21,5,3,4,0,6,33]"""


max_lista = 10
from random import randint

x = []
y = []


def gravar_lista_x():
    for i in range(max_lista):
        x.append(randint(1, 10))

def gerar_lista_y():
    for i in range(max_lista):
        if i % 2 == 0:
            y.append(x[i] / 2)
        else:
            y.append(x[i] * 3)

gravar_lista_x()
gerar_lista_y()
print("\nLista X: ", x)
print("\nLista Y: ", y)
