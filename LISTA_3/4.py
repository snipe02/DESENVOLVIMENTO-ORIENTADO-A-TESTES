"""4 Faça uma função que recebe por parâmetro o tempo de duração de um
processo em uma fábrica expressa em segundos e retorna também por
parâmetro esse tempo em horas, minutos e segundos."""

def tempo(segundos):
    if type(segundos) == int and segundos > 0:
      horas = segundos // 3600
      minutos = segundos // 60 - horas*60
      segundos = segundos - minutos*60 - horas*3600
      return horas, minutos, segundos
    else:
      return Exception

assert tempo(3600) == (1, 0, 0)
assert tempo(3660) == (1, 1, 0)
assert tempo(3660.2) == Exception
assert tempo('') == Exception
assert tempo(True) == Exception
assert tempo(-982) == Exception
assert tempo(0) == Exception
print("todos OK")

