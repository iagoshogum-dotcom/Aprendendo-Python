calculadora = bool(1)

while calculadora
print("calculadora")
print("somar = 1")
print("subrair = 2")
print("multiplicar = 3")
print("dividir = 4")
print("sair = 5")

escolha = input()

while escolha == "1":
    print("soma")
    numero1 = float(input())
    print("+")
    numero2 = float(input())
    resposta = numero1+numero2
    print(resposta)

while escolha == "2":
    print("subtraçao")
    numero1 = float(input())
    print("-")
    numero2 = float(input())
    resposta = numero1-numero2
    print(resposta)