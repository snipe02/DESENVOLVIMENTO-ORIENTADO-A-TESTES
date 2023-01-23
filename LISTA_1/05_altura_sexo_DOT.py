"""Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma fanção chamada peso ideal que receba a altura e o sexo via parâmetro e
que calcule e returne seu peso ideal,utilizado as seguintes fórmulas:"""

altura = float(input("Digite altura "))
sexo = int(input("Digite o sexo "))

def peso_ideal(altura, sexo):  #ALTURA E SEXO SÃO PARÂMETROS DESSA FUNÇÃO.
    if sexo == 1:
        ideal_mulher = (62.1*altura)-44.7
        return ideal_mulher

    elif sexo == 2:
        ideal_homem = (72.7*altura)-58
        return ideal_homem

ch = peso_ideal(altura,sexo)

print(ch)






