lista_nomes = ['lucas', 17, 19, 100, 23]


def excluir(lista_nomes, name):
    if name in lista_nomes:
        lista_nomes.remove(name)
    else:
        print('Este nome não exite na lista')

def alterar(lista_nomes, y, x):
    for c in range(len(lista_nomes)):
        if y in lista_nomes:
            recebe_nome = lista_nomes.index(y)
            lista_nomes[recebe_nome] = x

def main():
    nome = str(input())
    indice = int(input())
    other = str(input())
    ch = excluir(lista_nomes, nome)
    print(ch)

if __name__=='__main__':
    main()