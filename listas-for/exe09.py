from idlelib.replace import replace

while True:
    print("----------- Calculadora ------------")

    print("1 subtrair valores")
    print("2 somar valores")
    print("3 multiplicar valores")
    print("4 dividir valores")
    print("5 sair")
    print("------------------------------------")
    escolha = input("qual tipo de calculo quer realizar?")
    if escolha == 5:
        break
    match escolha:
        case 1:
            numero1 = float(input("primeiro valor"))
            numero2 = float(input("segundo valor"))
            print(f"O resultado é {numero1 - numero2}")
        case 2:
            numero1 = float(input("primeiro valor"))
            numero2 = float(input("segundo valor"))
            print(f"O resultado é {numero1 + numero2}")
        case 3:
            numero1 = float(input("primeiro valor"))
            numero2 = float(input("segundo valor"))
            print(f"O resultado é {numero1 * numero2}")
        case 4:
            numero1 = float(input("primeiro valor"))
            numero2 = float(input("segundo valor"))
            if numero2 == 0:
                print("nao é possivel dividir por 0")
                break
            print(f"O resultado é {numero1 / numero2}")

