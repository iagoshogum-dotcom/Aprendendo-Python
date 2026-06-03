notasAlunos = [["João",8.7,9.0],
               ["Maria",7.3,9.0],
               ["José",8.3,5.2]]
mediaAlunos = []
for i in notasAlunos:
    list = [i[0],(i[1]+i[2])/2]
    mediaAlunos.append(list)
print(mediaAlunos)
