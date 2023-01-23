from random import randint
listaA = list()
listaB = list ()

def create():
    for c in range(2):
        load = randint(12,74)
        listaA.append(load)
        load_1 = randint(7,92)
        listaB.append(load_1)

listaC = list()
def ce(listaA, listaB):
    for c in range(2):
        listaC.append(listaA[c])
        listaC.append(listaB[c])

ch = create()
ch1 = ce(listaA, listaB)
print(listaA, listaB, listaC)
