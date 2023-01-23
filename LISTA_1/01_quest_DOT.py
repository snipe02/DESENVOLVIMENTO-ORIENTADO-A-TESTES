#faça uma funçao que recebe um número inteiro por parametro e return verdadeiro se ele for par e falso se for impar.#


def par_impar(n):
    if n % 2 == 0:
        return True
    else:
        return False

while True:
    try:
         num = int(input("Digite um numero: "))
         if par_impar(num) == True:
            print("\nO número %d é PAR." % num)
         else:
             print("\nO número %d é impar." % num)
         break
    except:
         print("\nNúmero invalido. Digite novamente!")
