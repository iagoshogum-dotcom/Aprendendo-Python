vendas = [1200.50, 3400.00, 980.00, 5600.20, 2100.00, 850.00]
vendasAcimaMedia = []

for v in vendas:
    media = sum(vendas) / len(vendas)
    if v > media:
        vendasAcimaMedia.append(v)

print(f"a media de vendas é de {media} e os valores que estao acima da media sao {vendasAcimaMedia}")
