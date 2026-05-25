anoNasc = []
maioridade = []
menoridade = []
continuar = input("Quer começar a perguntar as datas de nascimento? (s/n)").upper()[0]

while continuar == "S" or continuar == "C":
    ano = int(input("Em que ano voce nasceu?"))
    anoNasc.append(ano)
    continuar = input("Quer continuar (s/n)").upper()[0]

for a in anoNasc :
    idade = 2026 - a
    if idade >= 18 :
        maioridade.append(idade)
    else:
        menoridade.append(idade)

print(f"as idades de maior sao {maioridade} contando {len(maioridade)} pessoas de maior idade")
print(f"as idades de menor sao {menoridade} contando {len(menoridade)} pessoas de menor idade")