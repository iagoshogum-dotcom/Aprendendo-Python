vendas = [

    [1200, 850, 900, 1500],

    [900, 1100, 1000, 1300],

    [1500, 1600, 1400, 1800],

    [700, 600, 800, 900]

]
matrizV = [sum(v) for v in vendas]
matrizD = [sum(d) for d in zip(*vendas)]
print(f" soma das vendas de cada vendedor {matrizV}")
print(f" soma das vendas de cada dia {matrizD}")




