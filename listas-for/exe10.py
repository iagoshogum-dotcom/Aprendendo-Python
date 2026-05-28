import random
numeroSorteado = random.randint(1,20)
numeroEscolhido = int(input("tente adivinhar o numero que pensei"))

while numeroSorteado != numeroEscolhido:
    if numeroEscolhido > numeroSorteado  :
        print("o numero é menor do que voce escolheu")
    else:
        print("o numero é maior do que voce escolheu")

    numeroEscolhido = int(input("tente novamente"))

print("parabens voce acertou, Cagao :C")