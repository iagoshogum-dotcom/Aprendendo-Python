valorCa = 10.00
valorBa = 12.00
valorXsalada = 15.00
valorHam = 13.00
print("cardapio lanchonete\n\n ----------------------- \n 100: Cachorro-Quente \n 101: Bauru Simples \n 102: X-Salada \n 103: Hambúrguer \n --------------------------------")

while True :
    codigo =int(input("digite o codigo do produto"))
    match codigo:
        case 100:
            print(f"cachorro quente no valor de {valorCa}")
        case 101:
            print(f"Bauru Simples no valor de {valorBa}")
        case 102:
            print(f"X-Salada no valor de {valorXsalada}")
        case 103:
            print(f"Hambúrguer no valor de {valorHam}")
        case _:
            print(f"código de produto invalido")

