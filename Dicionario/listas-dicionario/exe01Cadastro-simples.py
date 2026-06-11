pessoa = {
    "nome":"iago",
    "idade":22,
    "cidade":"brasilia"
}
for chave,valor in pessoa.items():
    if chave == "nome" or chave == "cidade":
        print(chave,valor)