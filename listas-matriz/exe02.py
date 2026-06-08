estoque = [[12, 5, 8],
            [3, 15, 2],
            [19, 0, 7]]

linha,coluna = input("selecione linha e coluna").split()
print(f"a caixa do seu estoque é a caixa {estoque[int(linha)-1][int(coluna)-1]}")





