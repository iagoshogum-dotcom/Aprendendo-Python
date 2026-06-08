numero = int(input("digite um numero"))
list = []

for i in range(0 , 10):
    numero *= i+1
    list.append(numero)
print(list)
