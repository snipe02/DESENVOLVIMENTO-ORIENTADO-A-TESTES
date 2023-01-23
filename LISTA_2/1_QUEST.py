"""Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
a) Mostre a quantidade de números pares;
b) Grave uma lista somente com os números pares e mostre a lista;
c) Mostre a quantidade de números ímpares;
d) Grave uma lista somente com os números ímpares e mostre a lista."""


max_lista = 10
l = list(range(max_lista))
#1 = []
l_p = []
l_i = []
from random import *

def gravar_lista():
    for i in range(max_lista):
#        l[1] = int(input("\nDigite o %dº numero: " % (i+l)))
        l[i] = randint(-100,100) #         gera numeros inteiros aleatorios
#        l[i] = uniform(-100,100)          gera numero reais aleatorios
#          l.append(randint(100,100))

#a)

def quant_pares():
    cont_p = 0
    for i in range (max_lista):
        if l [1] % 2 == 0:
            cont_p +=1
    return cont_p

#b)

def gerar_lista_pares():
    for i in range (max_lista):
        if l[i]% 2 == 0:
           l_p.append(l[i])

#c)

def quant_impares():
    cont_i = 0
    for i in range (max_lista):
        if l[i] % 2 != 0:
           cont_i += 1
    return cont_i

#d)
def gerar_lista_impares():
    for i in range (max_lista):
        if l[i]% 2 != 0:
           l_i.append(l[i])

gravar_lista()
print("\nQuantidade de numeros é: %d." % quant_pares())
gerar_lista_pares()
print("\nQuantidade de numeros impares: %d." %quant_impares())
gerar_lista_impares()
print("Lista L: ", l)
print("Pares Lista l_p): ",l_p)
print("impares (Lista l_i): ",l_i)

