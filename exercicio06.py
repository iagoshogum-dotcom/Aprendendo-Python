print("-------------------------------------------------------------------------")
print("                              triangulos                                 ")
print("-------------------------------------------------------------------------")


lado1 = float(input("qual a medida do primeira aresta de seu triangulo?"). replace(",", "."))
lado2 = float(input("da segunda aresta?"). replace(",", "."))
lado3 = float(input("da terceira aresta?"). replace(",", "."))

if lado1+lado2<lado3 or lado3+lado2<lado1 or lado1+lado3<lado2 :
    print("Lamento mas isso nao é um triangulo :C")
else:
    if lado1 == lado2 == lado3 :
        print("seu triangulo é equilatero pois todas as medidas sao iguais")
    elif lado1 != lado2 != lado3 :
        print("seu triangulo é escaleno pois todas as medidas sao diferentes")
    else:
        print("seu triangulo e isosceles")