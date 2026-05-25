listaIdades = []
continuar = input("Quer começar a perguntar idades? (s/n)").upper()[0]

while continuar == "S" or continuar == "C":
    idade = int(input("digite sua idade"))
    listaIdades.append(idade)
    continuar = input("Quer continuar? (s/n)").upper()[0]

print(listaIdades)
