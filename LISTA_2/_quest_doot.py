def verificar_caracteres(frase_ori):
  frase_correta = list(range(len(frase_ori)))
  for i in range(len(frase_ori)):
      frase_correta[i] = frase_ori[i]
      while (frase_correta[i] < "A" or frase_correta[i] > "Z"):
        print("\nCaractere digitado não é letra: %s" % frase_ori[i])
        frase_correta[i] = input("Digite novamente uma letra qualquer: ").upper()
  return frase_correta

def quant_letra():
    cont_a = 0
    for i in range(len(frase)):
        if frase[i] == "A":
           cont_a += 1
    return cont_a
frase = input("\nDigite uma sequência qualquer de caracteres: ").upper()
frase = verificar_caracteres(frase)
print("Caracteres digitados: ", frase)
print("Quantidade de letras 'A' digitadas: %d" % quant_letra())
#ou
print("Quantidade de letras 'A' digitadas: %d" % frase.count("A"))