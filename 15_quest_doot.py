"""15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E."""

from random import randint

listaD =[]
listaE =[]
for c in range(10):
    numero = randint(10,30)
    listaD.append(numero)

for s in listaD:
    listaE.insert(0,s)

print(listaD)
print(listaE)



