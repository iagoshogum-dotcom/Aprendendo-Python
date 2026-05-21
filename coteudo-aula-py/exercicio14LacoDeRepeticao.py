numeros = (1,2,3,3,4)

for n in numeros :
    print(numeros)

print("-------------------------")

for x in range(0, 51):
    print(x)

print("-------------------------")

print("-----    chamada    -----")

alunos = ["Jaqueline", "Débora", "Evilyn", "Arthur", "Izaac", "Escobar", "Rafael", "Luã", "Lindoso", "Wojcieskovsky"]
alunos.sort()


print(f"Quantos alunos tem na sala: {len(alunos)}")

print("--- Iniciando chamada ---")

for i in alunos:
    print(f"Aluno(a) {i} esta presente!")
print("--- Fim da chamada ---")