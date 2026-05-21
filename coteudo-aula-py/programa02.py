frequencia = int(input("Frequencia do aluno"))

if frequencia > 0 :
    nota1 = float(input("Nota primeiro bimestre").replace(",","."))
    nota2 = float(input("Nota segundo bimestre").replace(",","."))

    media = (nota1 + nota2)/2

    if media >= 7 :
        print("Aluno reprovado")
    elif media >= 5 :
        print("Aluno de recuperacao")
        notRec = float(input("Nota da recuperacao"))
        if notRec >=5 :
            print("Aprovado na recuperacao")
        elif notRec <=5 :
            print("Fazer provao de fim de ano")
            notPV = float(input("Nota do Provao de fim de ano"))
            if notPV >= 8 :
                print("Aluno aprovado na materia")
            else :
                print("Aluno reprovado na materia")
    else :
        print("Aluno reprovado")
else :
    print("Aluno nao compareceu as aulas")


