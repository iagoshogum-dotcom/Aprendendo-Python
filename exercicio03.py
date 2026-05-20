print("-------------------------------------------------------------------------")
print("                            MAIOR E MENOR                                ")
print("-------------------------------------------------------------------------")

numero2 = float(input("Qual o primeiro numero para compararmos"))
numero3 = float(input("qual é o segundo numero"))

if numero2 < numero3 :
    print("o numero {} é menor que o numero {}".format( numero2, numero3))
elif numero2 == numero3 :
    print("os numeros sao iguais")
else:
    print("o numero {} é menor que o numero {}".format(numero3, numero2))