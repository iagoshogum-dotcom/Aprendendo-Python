carrinho = []
print("vamos começar as compras")
while True :
    compra = input("o que deseja adicionar ao carrinho? ou deseja sair?")
    carrinho.append(compra)
    if compra == "sair":
        break

carrinho.sort()
carrinho.pop()
print(carrinho)
