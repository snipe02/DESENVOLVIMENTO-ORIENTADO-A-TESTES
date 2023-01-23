"""Prova1_q2. Faça um programa que:
a) Tenha uma função que alimente (grave) uma lista com um número de posições definidas pelo usuário. Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
b) Tenha uma função que receba um nome por parâmetro e altere esse nome pra um novo nome;
c) Tenha uma função que receba um nome como parâmetro e exclua esse nome da lista.
Obs: todas as funções devem ser chamadas do programa principal. """


def gravar_nomes():
   nomes = []
   quantidade = int(input("\nDigite a quantidade de elementos da lista: "))
   for i in range(quantidade):
      nome = input("\nDigite o nome da pessoa: ")
      nomes.append(nome)
      print("\nInclusão com sucesso!")

def alterar_nome(nome):
   pos = -1
   for i in range(len(nomes)):
      if nome == nomes[i]:
         pos = i
         break
   if pos >= 0:
      print("\nNome anterior: %s." % (nome))
      novo_nome = input("\nNome atual: ")
      nomes[pos] = novo_nome
      print("\nAlteração realizada com sucesso")
   else:
      print("\nO nome não está na lista!")

def excluir_nome(nome):
   pos = -1
   for i in range(len(nomes)):
      if nome == nomes[i]:
         pos = i
         break
   if pos >= 0:
      del nomes[pos]
      print("\nO nome %s foi excluido com sucesso." % (nome))
   else:
         print("\nO nome não está na lista!")

gravar_nomes()
nome = input("\nDigite o nome a alterar: ")
alterar_nome(nome)
nome = input("\nDigite o nome a excluir: ")
excluir_nome(nome)
print(nomes)