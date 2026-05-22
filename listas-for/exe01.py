print("-------------------------------------------------------------------------")
print("                     funçoes matematicas e for                           ")
print("-------------------------------------------------------------------------")

numeros = []

for i in range(1, 7):
    numero = int(input(f"digite o {i} numero"))
    numeros.append(numero)

print(f"os numeros de sua lista sao {numeros}")
print(f"a soma de todos os numeros de sua lista sao {sum(numeros)}")
print(f"o maior numero de sua lista é {max(numeros)}")
print(f"o menor numero de sua lsita é {min(numeros)}")

