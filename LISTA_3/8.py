""""8. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
ou negativo. A função deve retornar um valor booleano."""

def pos_neg(valor):
  if type(valor) != int:
    return Exception

  else:
    if valor >= 0:
      return True
    else:
      return False

assert pos_neg(4) == True
assert pos_neg(-5) == False
assert pos_neg(7.1) == Exception
assert pos_neg('oito') == Exception
assert pos_neg(0) == True
print("todos oK")
