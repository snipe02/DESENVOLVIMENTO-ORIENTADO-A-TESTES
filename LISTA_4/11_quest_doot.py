"""11. Faça uma função que recebe, por parâmetro, a altura e o sexo de uma
pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a
fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura
- 44.7."""

def peso_ideal(altura,sexo):
    if type(altura) != float or type(sexo) != int:
        return Exception
    if altura <0:
        return Exception
    if sexo < 1 or  sexo >2:
        return Exception
    if sexo == 2:
        homem = (72.7*altura)-58.0
        return homem
    elif sexo == 1:
        mulher = (62.1*altura)-44.7
        return mulher.__round__(3)


assert peso_ideal(1.85,2) == 76.495
assert peso_ideal(2, 1) == Exception
assert peso_ideal(1.85, 1.4) == Exception
assert peso_ideal(1.67, 3) == Exception
assert peso_ideal(1.34, 0) == Exception
assert peso_ideal(1.60, 1) == 54.660
assert peso_ideal('1 metro',2) == Exception
assert peso_ideal(1.23, True) == Exception
assert peso_ideal(1.70, 1) == 60.87
assert peso_ideal(0,1) == Exception
assert peso_ideal(-1.45, 2) == Exception
print("todos os testes estao ok")



