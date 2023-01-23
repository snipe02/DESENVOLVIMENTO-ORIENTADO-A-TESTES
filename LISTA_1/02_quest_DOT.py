""" Escreva um programa que lei o raio de um circulo e faça duas funções: uma função chamada área que calcule e returna a área#
do circulo e outra função perimetro que calcula e returna e perimentro do circulo.
            Area = PI * r2; Perimetro = PI * 2 * r; """


def area(r):
    return 3.14 * r**2
def perimetro(r):
    p = 3.14 * 2 * r
    return

while True:
    try:
        raio = float(input("Digite o raio do circulo: "))
        print("Á area do circulo é: %.2f" % area(raio))
        print("O perimetro do circulo é %.2f: " %perimetro(raio))
        break
    except:
        print("Raio. Digite novamente!")
