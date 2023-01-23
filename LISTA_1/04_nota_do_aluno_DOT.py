""" Escreva um programa para ler as notas das duas avaliaçães de um aluno no semestre. Faça um procedimento que receba as duas notas por parâmentro e calcule
e escreve a mádia minima para aprovação)."""


nota1 = float(input())
nota2 = float(input())

def media(x, y):
     resultado = (x + y ) / 2
     if resultado >= 6:
        return  (f" voce foi{resultado} reprovado")
     else:
        return  (f" voce foi{resultado} aprovado")

print(media,nota1,nota2)



