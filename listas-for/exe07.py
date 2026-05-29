comecar = "s"

while comecar == "s":
    numero = float(input("digite o numero desejado para anotarmos"))
    if numero > 10 or numero < 0 :
        comecar = input("isso nao é um numero valido digite um de acordo com o pedido certo? (s/n)")
    else:
        print(f"numero {numero} anotado ")
        break