print("-------------------------------------------------------------------------")
print("                          compra e desconto                              ")
print("-------------------------------------------------------------------------")

valueProduct = float(input("Valor da compra"))

if valueProduct>100 and valueProduct<=300 :
    sale5 = valueProduct * 0.05
    valueProduct -= sale5
    print(f"com desconto de 5% no valor de {sale5} pagara {valueProduct}")
elif valueProduct>300 and valueProduct<=500 :
    print(f"com desconto de 10% no valor de {valueProduct*0.1} pagara {valueProduct*0.9}")
elif valueProduct>500 :
    desconto15 = valueProduct * 0.15
    valueProduct -= desconto15
    print(f"com desconto de 15% {valueProduct}")
else:
    print("sem desconto")