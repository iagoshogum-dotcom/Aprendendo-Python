maioresDe18 = []
generoM = []
generoFmenorDe20 = []

pessoaCadastro = "s"

while pessoaCadastro == "s":
    idade = int(input("qual a idade?"))
    genero = input("qual o genero?").upper()

    if genero == "M":
        generoM.append(genero)

    if idade > 18 :
        maioresDe18.append(idade)

    if genero == "F" and idade < 20:
        generoFmenorDe20.append(genero+str(idade))

    pessoaCadastro = input("a mais cadastros a fazer? (s/n)")

print(f"a quantidade de pessoas maiores de 18 sao {len(maioresDe18)}")
print(f"a quantidade de pessoas de genero masculino sao {len(generoM)}")
print(f"a quantidade de pessoas de genero femenino e menores de 20 anos sao {len(generoFmenorDe20)}")



