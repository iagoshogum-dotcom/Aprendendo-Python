usuario = input("Digite o usuario").upper()
while True:
    match usuario:
        case "ADMIN":
            print("Acesso total: Criar, Ler, Atualizar e Deletar")
            break
        case "GERENTE":
            print("Acesso gerencial: Criar, Ler e Atualizar")
            break
        case "EDITOR":
            print("Acesso de conteúdo: Ler e Atualizar")
            break
        case "VISITANTE":
            print("Acesso de conteúdo: Ler")
            break
        case _:
            print("Perfil não reconhecido. Acesso bloqueado")
            break







