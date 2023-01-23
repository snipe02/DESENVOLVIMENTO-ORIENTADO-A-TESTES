from random import randint

def grave():
    lista=[]
    for c in range(15):
        lista.append(randint(1,50))
    return lista

def ler_lista_maior():
    lista_lida = grave()
    maior = -9999999
    for c in lista_lida:
        if c > maior:
            maior = c
    return maior

ch1 = grave()
ch2 = ler_lista_maior()
print(ch1)
print(ch2)