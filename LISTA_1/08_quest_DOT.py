def caractere(x):
    while x not in (' S ', ' s ','N','n'):
        x = input("Caracterista invalida.Digite novamente: ")
    return x

while True:
    try:
        num = int(input("Digite um número: "))
        print("O cubo do numero %d é %d" % (num, num**3))
        x = input("Deseja continuar (S- Sim ou N - Não)?? ")
        if caractere(x) in ('N'',''n'):
            break
    except:
        print("Numero invalida.DIgite novamente!")