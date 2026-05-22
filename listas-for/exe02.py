print("-------------------------------------------------------------------------")
print("                          notas aluno e for                              ")
print("-------------------------------------------------------------------------")

notas = []

for i in range(1, 5):
    nota = float(input(f"qual a nota  do {i} bimestre?"))
    notas.append(nota)

media = sum(notas)/len(notas)

if media >= 7 :
    print(f"O aluno foi a aprovado com a media de {media}")

else:
    print(f"O aluno ficou de recuperação com a media de {media}")