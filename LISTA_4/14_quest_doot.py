"""14. Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se
esses valores podem ser os comprimentos dos lados de um triângulo e, neste
caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um
triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento
de cada lado de um triângulo é menor do que a soma do comprimento dos outros
dois lados. O procedimento deve identificar o tipo de triângulo formado
observando as seguintes definições:

o Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
o Triângulo Isósceles: os comprimentos de 2 lados são iguais.
o Triângulo Escaleno: os comprimentos dos 3 lados são diferentes."""


def triangulo(x, y, z):
  if type(x or y or z) != int or float:
    return Exception
  if x or y or z < 0:
    return Exception

assert triangulo(5, 5, 'sete') == Exception
assert triangulo(True, 5, 4) == Exception
assert triangulo(-4, 5, 5) == Exception

print('Todos os testes estão OKS')

