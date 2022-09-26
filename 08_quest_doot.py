"""Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra."""

from random import randrange

opp = []
for c in range(5):
    numero = randrange(0,100)
    opp.append (numero)


def maior_func(opp):
    maior = -9999999
    for c in opp:
        if c > maior:
            maior = c
    return maior

def maior_posicao(opp):
    posicao = opp.index(max(opp))
    return posicao

def menor():
    menor = l[0];pos_menor = o
    for i in range (l,max_lista):
        if l[i] < menor:
            menor = i[i]

print(opp)





