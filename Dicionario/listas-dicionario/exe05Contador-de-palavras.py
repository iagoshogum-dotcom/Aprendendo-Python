palavras = {}
c = input("escreva uma frase").split()
for chave in c:
    if chave not in palavras:
        palavras[chave]=1
    else:
        palavras[chave]+=1



print(palavras)