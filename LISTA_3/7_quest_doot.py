"""7 )Faça uma função que recebe a idade de um nadador por parâmetro e retorna
a categoria desse nadador de acordo com a tabela abaixo:
Idade Categoria
5 a 7 anos Infantil A
8 a 10 anos Infantil B
11-13 anos Juvenil A
14-17 anos Juvenil B
Maiores de 18 anos
(inclusive)"""

def definir_categoria(idade):
    if type(idade) != int:
        return Exception
    if idade >= 5 and idade <= 7:
        categoria = "Infantil A"
    elif idade >= 8 and idade <=10:
        categoria = "infanitl B"
    elif idade >= 11 and idade <= 13:
        categoria = "javenil A"
    elif idade >= 14 and idade <= 17:
        categoria = "javenil B"
    elif idade >= 17 and idade <= 120:
        categoria = "adulto"
    else:
        return Exception
    return categoria
assert definir_categoria("*") == Exception
assert definir_categoria(-1) == Exception
assert definir_categoria(10.35) == Exception
assert definir_categoria(4) == Exception
assert definir_categoria(400) == Exception

print('Todos OK')
