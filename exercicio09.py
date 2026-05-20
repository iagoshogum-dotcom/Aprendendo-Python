print("-------------------------------------------------------------------------")
print("                           atletas e tamanho                             ")
print("-------------------------------------------------------------------------")

idade = int(input("digite a idade para classificar"))

if idade <= 9 :
    print("tamanho mirim")
elif idade <= 14 :
    print("tamanho infantil")
elif idade <= 19 :
    print("tamanho junior")
elif idade <= 25 :
    print("tamanho senior")
else:
    print("tamanho master")
