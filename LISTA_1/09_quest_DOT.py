def soma_intervalo(a,b):
    soma = 0
    for i in range(a,b+1):
        soma += i
        return soma

while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        if n1 <= n2:
            print("na soma do intervalo informado é",soma_intervalo(n1,n2))
            break
        else:
            print("n2 deve ser maior que n1. Digite novamente!")
    except:
        print("valor invalido. Digite novamente!")