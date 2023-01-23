"""10. Faça uma função que recebe a média final de um aluno por parâmetro e
retorna o seu conceito, conforme a tabela abaixo:
Nota Conceito
de 0,0 a 4,9 D
de 5,0 a 6,9 C
de 7,0 a 8,9 B
de 9,0 a 10,0A"""

def media(media_final):
  if type(media_final) != float:
    return Exception
  
  else:
    if media_final >= 7.0 and media_final <= 8.9:
      return 'B'
    elif media_final >= 0.0 and media_final <= 4.9:
      return 'D'
    elif media_final >= 5.0 and media_final <= 6.9:
      return 'C'
    elif media_final >= 9.0 and media_final <= 10.0:
      return 'A'

assert media(7.0) == 'B'
assert media(7) == Exception
assert media(-9) == Exception
assert media(2.3) == 'D'
assert media(5.5) == 'C'
assert media(10.0) == 'A'
assert media('nota boa') == Exception
assert media(False) == Exception
print("todos OK")