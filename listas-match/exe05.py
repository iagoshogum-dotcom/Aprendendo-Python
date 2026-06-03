while True:
    mes = input("digite o mes que deseja saber a estação").lower()
    match mes:
        case "junho"|"julho"|"agosto"|"6"|"7"|"8":
            print("este mes pertence a estação de inverno")
        case "março"|"abril"|"maio"|"3"|"4"|"5":
            print("este mes pertence a estação de outono")
        case "setembro"|"outubro"|"novembro"|"9"|"10"|"11":
            print("este me pertence a estação de primavera")
        case "dezembro"|"janeiro"|"fevereiro"|"12"|"1"|"2":
            print("este mes pertence a estação de verão")
        case _:
            print("esse nao é um valor valido")

