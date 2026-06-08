matriz_base = [[1, 2], [3, 4]]
fator = int(input("digite um numero para multiplicar por todos os que estao dentro da matriz"))
matrizMultiplicada = []
for i in matriz_base:
    for j in i :
        matrizLinha = []
        matrizLinha.append(j*fator)

print(matrizMultiplicada)
