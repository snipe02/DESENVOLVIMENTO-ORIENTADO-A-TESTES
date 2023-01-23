'''  A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes,
coletando dados sobre o salário e número de filhos. Faça uma função que leia
esses dados para um número não determinado de pessoas e retorne a média de
salário da população, a média do número de filhos, o maior salário e o percentual
de pessoas com salário até R$ 350,00.
'''
def pref(dic):
    if type(dic)!=dict or len(dic)==0:
        return Exception
    else:
        media = sum(dic.keys())/len(dic)
        media_f  = sum(dic.values())/len(dic)
        maior = max(dic.keys())
        soma=0
        for i in dic.keys():
            if i>=350:
                soma+=1
        porcen=round((soma/len(dic))*100)
        return media, media_f, maior, porcen

print(pref({12:2,350:3,13:1}))
assert pref({1:2})==(1,2,1,0)
assert pref({})==Exception
assert pref({35:1,35:3,30:5})==(32.5,4,35,0)
assert pref({350:1,350:3,350:5})==(350,5,350,100)
print('teste Ok')