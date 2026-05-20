print("-------------------------------------------------------------------------")
print("                        JOVEM, ADULTO OU VELHO                           ")
print("-------------------------------------------------------------------------")

nasc = int(input("Qual sua data de nascimento"))

idade =  2026 - nasc

if idade < 18 :
    print("voce é jovem")
elif idade >= 60 :
     print("voce é velho")
else:
     print("voce é calvo")