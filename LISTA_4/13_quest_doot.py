'''13. Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de
término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos.
O procedimento deve retornar, também por parâmetro, a duração do jogo em
horas e minutos, considerando que o tempo máximo de duração de um jogo é
de 24 horas e que o jogo pode começar em um dia e terminar no outro.
'''


def tempo(h1, m1, h2, m2):
    if type(h1) != int or type(m1) != int or h1 > 24 or m1 > 60 or type(h2) != int or type(m2) != int or h2 > 24 or m2 > 60:
        return Exception
    else:
        if h1 < h2:
            h = h2-h1
            if m1 < m2:
                m = m2-m1
            else:
                m = m1-m2
        else:
            h = h1-h2
            if m1 < m2:
                m = m2-m1
            else:
                m = m1-m2
        return f'{h}:{m}'


print(tempo(1, 2, 3, '4'))
assert tempo(2, 1, 3, 4) == ('1:3')
assert tempo(1, 2, 3, 4) == '2:2'
assert tempo('1', 2, 3, 4) == Exception
assert tempo(1, 2, 3, '4') == Exception
assert tempo(61,2,3,4)==Exception
assert tempo(24,1,2,61)==Exception
print('Teste Ok')
