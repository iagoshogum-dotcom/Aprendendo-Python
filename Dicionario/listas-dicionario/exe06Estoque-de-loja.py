estoque = {"Teclado": 15, "Mouse": 22, "Monitor": 8}
carrinho = {}
while True:
    produto,quantidade = input("escolha o produto e a quantidade disponivel").split()
    carrinho[produto]=int(quantidade)
    for c,v in estoque.items():
        for k,y in carrinho.items():
            refeito = v - y
            carrinho[k]=refeito
            estoqueA = estoque|carrinho
        print(estoqueA)

