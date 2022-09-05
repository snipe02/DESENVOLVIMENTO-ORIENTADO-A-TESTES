"""Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma fanção chamada peso ideal que receba a altura e o sexo via parâmetro e
que calcule e returne seu peso ideal,utilizado as seguintes fórmulas:"""


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
