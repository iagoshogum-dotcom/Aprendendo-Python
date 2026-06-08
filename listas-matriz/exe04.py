
matriz_base = [[1, 2], [3, 4],[3, 4]]
fator = int(input("digite o numero fator"))
matrix = []
for i in matriz_base:
    lista = []
    for j in i:
        lista.append(j*fator)
    matrix.append(lista)
print(matrix)