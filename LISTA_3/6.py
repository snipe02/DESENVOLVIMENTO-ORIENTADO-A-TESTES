"""6. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
um valor booleano."""

def perfect(value):
  if type(value) != int:
    return Exception
  else:
    divider = 0
    for c in range(1,value):
      if value%c == 0:
            divider += c
    if divider == value:
      return True
    else:
      return False    
    
assert perfect(6) == True
assert perfect(3) == False
assert perfect(4.3) == Exception
assert perfect('sete') == Exception
assert perfect(True) == Exception
assert perfect(7) == False
print("todos OK")