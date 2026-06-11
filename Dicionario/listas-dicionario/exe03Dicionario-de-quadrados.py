quadrados  = {}
for numeros in range(1, 6):
    quadrados.setdefault(numeros,numeros**2)
print(quadrados)
for k,v in quadrados.items():
    print(k,v)