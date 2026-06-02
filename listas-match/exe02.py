while True:
    numero = int(input("escolha um numero de 1 a 7 para achar o correspondente"))
    match numero:
        case 1:
            print("corresponde ao dia de domingo da semana")
        case 2:
            print("corresponde ao dia de segunda da semana")
        case 3:
            print("corresponde ao dia de terça da semana")
        case 4:
            print("corresponde ao dia de quarta da semana")
        case 5:
            print("corresponde ao dia de quinta da semana")
        case 6:
            print("corresponde ao dia de sexta da semana")
        case 7:
            print("corresponde ao dia de sabado da semana")
        case _:
            print("dia invalido")