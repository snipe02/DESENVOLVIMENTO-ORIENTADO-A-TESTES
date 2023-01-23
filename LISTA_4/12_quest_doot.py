"""12. Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os
ordenados em ordem crescente."""


def crescente(x, y):
  if type(x) != int or type(y) != int:
    return Exception
  elif x < 0 or y < 0:
    return Exception
  else:
    if x > y:
      return y, x
    else:
      return x, y

assert crescente(5, 3) == (3, 5)
assert crescente(3, 5) == (3, 5)
assert crescente(4.34, 2) == Exception
assert crescente(-3, 4) == Exception
assert crescente(15, 7) == (7, 15)
assert crescente('oito', False) == Exception
assert crescente(0,10) == (0,10)
assert crescente([2,3,4,1], 7) == Exception