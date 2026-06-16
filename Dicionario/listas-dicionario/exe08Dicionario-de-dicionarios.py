import random
compatriotas = {}
cadastrar = "s"
while cadastrar == "s":
    id = random.randint(1000,9999)
    nome = input("digite o nome do compatriota")
    cargo = input("digite o cargo do compatriota")
    salario = int(input("digite o salario do compatriota"))

    compatriotas[id]={
        "nome" : nome,
        "cargo" : cargo,
        "salario" : salario
    }
    cadastrar = input("deseja cadastrar outro funcionario? s/n ")

for id,dados in compatriotas.items():
    if dados["salario"] > 3000:
        print(f"{dados["nome"]} - {dados["cargo"]} ")
