Escreva um programa para ler o numero



lados = int(input())
centimetro = float(input())

def tamanho(l,c):
    if l == 3:
        perimetro = l*c
        return f'TRIÂNGULO, {perimetro} centímetros'

    elif l == 4:
        area = c*c
        return f'QUADRADO, {area}cm²'

    elif l == 5:
        return 'PENTAGONO'

ch = tamanho(lados,centimetro)

print(ch)