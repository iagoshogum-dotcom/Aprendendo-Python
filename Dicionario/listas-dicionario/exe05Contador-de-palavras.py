from shlex import split

palavras = {}
v = input("escreva uma frase").split()
for c,v in palavras.items():
    c += 1
    palavras.setdefault(c,v)
print(palavras)