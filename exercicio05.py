print("-------------------------------------------------------------------------")
print("                                  IMC                                    ")
print("-------------------------------------------------------------------------")

numeroP = float(input("qual seu peso?").replace(",", "."))
numeroA = float(input("qual sua altura?").replace(",", "."))

imc =  numeroP / (numeroA * numeroA)

print("seu imc é {} kg/m2". format(imc))