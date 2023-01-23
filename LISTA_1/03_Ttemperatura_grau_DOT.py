# Escreva um programa para ler uma temperatura em graus Fahrenhaeit. Faça uma função chamada celsius para calcular
# e returnar o valor correspondete em graus celsius.#
       #  Fórmula: C = ((F-32)/9)*5 #

fah = float(input("Temperatura Fahrenhaeint:\n "))

def celsius_func(fah):
    celsius = ((fah-32)/9) * 5
    return celsius.__round__(5)

ch = celsius_func(fah)

print(ch)
