'''14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
Escrever a lista C modificada.'''


from random import randint

lista =[]
for i in range(10):
    numero = randint(-20,20)
    lista.append(numero)

print(lista)

for d in range(len(lista)):
    if lista[d] < 0:
        lista[d] = 0

print(lista)






