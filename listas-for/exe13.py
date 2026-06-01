carrinho = []
print("vamos começar as compras")
while True :
    compra = input("o que deseja adicionar ao carrinho? ou deseja sair?")
    if compra == "sair":
        break
    carrinho.append(compra)

carrinho.sort()
print(carrinho)
