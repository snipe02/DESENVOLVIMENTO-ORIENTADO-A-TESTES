from random import randint
listaX =[]
listaY=[]
listaY_nova =[]
for c in range(10):
    num = randint(1,100)
    listaX.append(num)


for d in range(10):
    numero = randint(1,100)
    listaY.append(numero)


for i, v in enumerate(listaY):
    if i % 2 == 0:
        listaY_nova.append(listaX[i]/2)
    else:
        listaY_nova.append(listaX[i]*3)

print(listaX)
print(listaY)
print(listaY_nova)