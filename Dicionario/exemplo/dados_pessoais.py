dados_pessoais = {
    "nome":"joao",
    "nascimento":"20-05-2005",
    "sexo":"M",
    "altura": 1.70,
    "temCNH": True
}
#dados_pessoais["altura"] = 1.85
#dados_pessoais["peso"] = 70
#dados-pessoais.setdefaut("peso",80)
#dados_pessoais.pop("sexo")

continuar = "s"
while continuar == "s":
    novaChave, novoValor = input("digite uma nova chave e uma novo valor ou atualize algum dado, separando por virgula").split(",")
    dados_pessoais[novaChave] = novoValor
    print(dados_pessoais.keys())
    dado = input("escolha o dado")
    print(dados_pessoais.get(dado, "Valor não encontrado!"))
    continuar = input("voce quer continuar a procurar dados: (s/n)").lower()