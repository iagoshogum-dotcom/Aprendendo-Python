idade = []
genero = []
idadesMaior18 = []
generosMas = []
pessoaCadastro = input("vamos começar a realizar cadastros? (s/n)")

while pessoaCadastro == "s":
    idadePer = int(input("qual sua idade"))
    idade.append(idadePer)
    generoPer = input("qual seu genero")
    genero.append(generoPer)
    pessoaCadastro = input("pessoa cadastrada com sucesso, quer realizar mais cadastros? (s/n)")

for i in idade:
    if i > 18 :
        idadesMaior18.append(i)
    for g in genero:
        if g == "M" :
            generosMas.append(g)





print(f"sao {len(generosMas)} pessoas de genero masculino")

print(f"sao {len(idadesMaior18)} pessoas de maiores")




