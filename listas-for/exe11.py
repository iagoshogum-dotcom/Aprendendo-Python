valor = int(input("qual o valor de saque"))
cedeluas = [50,20,10,5,2]
i = 0
while valor > 0 :
    qtd = valor // cedeluas[i]
    if qtd > 0:
        print(f"{qtd},{cedeluas[i]} ")
        valor = valor % cedeluas[i]
    i += 1
