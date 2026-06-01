ids_clientes = [101, 102, 103, 101, 104, 102, 105, 106, 103]
idsUnicos = []

for clientes in ids_clientes:
    if clientes not in idsUnicos:
        idsUnicos.append(clientes)

print(idsUnicos)