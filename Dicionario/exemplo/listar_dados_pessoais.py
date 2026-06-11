dados_pessoais = {
    "nome":"joao",
    "nascimento":"20-05-2005",
    "sexo":"M",
    "altura": 1.70,
    "temCNH": True,
    "idade":18
}

for chave,valor in dados_pessoais.items():
    print(f"{chave}:{valor}")

print(dados_pessoais.pop("peso", "Chave noa encontrada"))
print(dados_pessoais.pop("sexo", "Chave nao encontrada"))
print(dados_pessoais)
print(dados_pessoais.values())
print(dados_pessoais.popitem())
print(dados_pessoais.clear())
print(dados_pessoais)