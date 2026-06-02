while True:

    nota = input(f"Qual a nota a respeito do conceito do aluno?").upper()
    match nota:
        case "A":
            print(f"\033[35m Excelente trabalho \033[m")
        case "B":
            print("Bom desempenho")
        case "C":
            print("Satisfatório")
        case "D":
            print(f"Abaixo da média \033[31m (ATENÇÃO) \033[m")
        case "F":
            print("Reprovado")
        case _:
            print("Conceito invalido")