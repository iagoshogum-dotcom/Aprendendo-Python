import math

temperatura = "frio" #variavel

sala = ["monitor", "cadeira", 9, True, 18.5, "TV"] #vetor
print(sala[1].upper) #torna em maiusculo
print(sala[1].lower) #torna em minusculo

sala.pop() #remove o ultimo item da lista
sala.remove(9) #remove um item especifico da lista

""" #transforma tudo em uma string para que nao apareça no run
if temperatura == "frio":
    sala.append("AR")
    sala.append("teclado")

else:
    sala.append("caipirinha")
    sala.append(29.90)
"""


print(sala[-1]) #entre cochetes para especificar um item da lista em posiçoes
print(sala[1]) #posiçao

notas = [4.5, 2.8, 7.3, 8.5, 9.0]
soma = sum(notas) #sum para somar tudo dentro de um vetor
quantidade = len(notas) #len conta a quantia de componetes dentro do vetor

media = sum(notas)/len(notas)


print(soma)