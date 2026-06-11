produtos = {
    "banana":12.23,
    "barret 9mm":99.99,
    "olho humano":4.99,
}
escolha = input("o que deseja ver o preço")
print(produtos.get(escolha, "nao tem isso na minha lojina"))


