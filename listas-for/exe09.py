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

    if escolha == "1":
        print("subtraindo valores")
        numero1 = float(input("primeiro valor"))
        print("-")
        numero2 = float(input("segundo valor"))
        print(f"= {numero1 - numero2}")

    if escolha == "2":
        print("somando valores")
        numero1 = float(input("primeiro valor"))
        print("+")
        numero2 = float(input("segundo valor"))
        print(f"= {numero1 + numero2}")

    if escolha == "3":
        print("multiplicando valores")
        numero1 = float(input("primeiro valor"))
        print("x")
        numero2 = float(input("segundo valor"))
        print(f"= {numero1 * numero2}")

    if escolha == "4":
        print("dividindo valores")
        numero1 = float(input("primeiro valor"))
        print("/")
        numero2 = float(input("segundo valor"))
        print(f"= {numero1 / numero2}")

    if escolha == "5":
        break