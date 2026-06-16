estoque = {"Teclado": 15, "Mouse": 22, "Monitor": 8}

while True:
    produto, quantidade = input("Digite o produto e a quantidade desejada: ").split()

    quantidade = int(quantidade)

    if produto in estoque:
        if estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
            print("Compra realizada!")
            print(f"Estoque atualizado: {estoque}")
        else:
            print("Estoque insuficiente")
    else:
        print("Produto não encontrado")