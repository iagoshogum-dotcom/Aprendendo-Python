print("-------------------------------------------------------------------------")
print("                          decimal para binario                           ")
print("-------------------------------------------------------------------------")

decimais = [9, 18, 43, 126, 250, 352, 500]

for d in decimais:
    binario = bin(d)[2:]
    print(f"Decimal: {d} -> Binário: {binario}")