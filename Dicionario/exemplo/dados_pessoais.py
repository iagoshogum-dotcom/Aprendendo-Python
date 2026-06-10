dados_pessoais = {
    "nome":"joao",
    "nascimento":"20-05-2005",
    "sexo":"M",
    "altura": 1.70,
    "temCNH": True
}
print(dados_pessoais.keys())

continuar = "s"
while continuar == "s":
    dado = input("escolha o dado")
    print(dados_pessoais.get(dado, "Valor não encontrado!"))
    continuar = input("voce quer continuar a procurar dados: (s/n)").lower()