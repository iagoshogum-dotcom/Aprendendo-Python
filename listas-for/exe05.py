senhaCorreta ="iago123"

for s in range(1 ,4):
    senha =input("digite sua senha")
    if senha == senhaCorreta:
        print("Acesso permitido")
        break
    elif senha != senhaCorreta:
        print(f"Senha incorreta tente novamente"),[3]
        print(f"essa foi sua {s} tentativa")

else:
    print("Conta Bloqueada")
