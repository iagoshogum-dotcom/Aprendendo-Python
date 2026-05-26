comecar = input("vamos começar digite um numero de entre 0 e 10 entendeu? (s/n)")

while comecar == "s":
    numero = float(input("digite o numero desejado"))
    if numero > 10 or numero < 0 :
        comecar = input("isso nao é um numero valido digite um de acordo com o pedido certo? (s/n)")
    else:
        break
