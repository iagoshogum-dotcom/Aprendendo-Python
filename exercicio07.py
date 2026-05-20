print("-------------------------------------------------------------------------")
print("                           credito bancario                              ")
print("-------------------------------------------------------------------------")

salary = float(input("Qual o salario bruto do cliente?:").replace("," , "."))
installment = float(input("Qual o valor da parcela paga atuamente?:").replace("," , "."))

maxLimitInstallment = salary * 30 / 100

print(F"O valor maximo da parcela é de {maxLimitInstallment:2f}")

if installment > maxLimitInstallment :
    print("O credito foi recusado")
else:
    print("O credito foi aprovado")