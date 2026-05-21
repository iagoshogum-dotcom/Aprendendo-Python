numeros = []

for i in range(1, 7):
    numero = int(input(f"digite o {i} numero"))
    numeros.append(numero)

print(numeros)
print(sum(numeros))
print(max(numeros))
print(min(numeros))

