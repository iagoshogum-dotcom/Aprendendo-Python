print("-------------------------------------------------------------------------")
print("                         impares, pares e for                            ")
print("-------------------------------------------------------------------------")

numeros = []
impares = []
pares = []

for i in range(1, 11) :
    numero = int(input(f"Qual o {i} numero?"))
    numeros.append(numero)

print(f"numeros selecionados {numeros}")

for i in numeros :
    numero2 = i % 2
    if numero2 == 0 :
        pares.append(i)
    else:
        impares.append(i)

print(f"numeros impares dos selecionados {impares}")
print(f"numeros pares dos selecionados {pares}")