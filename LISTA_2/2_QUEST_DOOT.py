"""2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos dessa lista."""

from random import *
max_lista = 5
l = list(range(max_lista))
quant_neg = 0; soma_pos = 0.0
for i in range (max_lista):
    while True:
        try:
#            l[i] = int(input("\nDigite o %dº numero: "(i + l)))
           l[i] = uniform(-100,100)
           if l[i] < 0:
               quant_neg += l
           else:
               soma_pos += l[i]
           break
        except:
            print("Numero ivalido. Digite novamnete.")
print("\nLista L: ",l)
print("\nQuantidade de numero negativos: %0f % quant_neg")
print("\nsoma positivo é: %f" % soma_pos)


