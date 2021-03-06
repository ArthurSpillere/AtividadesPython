#######################################################################################################

# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor. 
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para 
# gerar numeros aleatórios, simulando os lançamentos dos dados. 

#######################################################################################################

from random import randint

lista = []
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0

for i in range(100):
    lista.append(randint(1, 6))

print(len(lista))
print(lista)

#Em vez da famosa tripa de if, você pode usar o método .count()
#Ex: lista.count(1) retorna quantas vezes o número 1 apareceu na lista
print(lista.count(1))
for num in lista:
    if num == 1:
        cont1 += 1
    elif num == 2:
        cont2 += 1
    elif num == 3:
        cont3 += 1
    elif num == 4:
        cont4 += 1
    elif num == 5:
        cont5 += 1
    elif num == 6:
        cont6 += 1

#Eu tento sempre seguir as boas práticas de programação e não passar da coluna80
#Que é exatamente onde o "80" da linha anterior acabou
#Você pode escrever de maneira organizada e pulando linhas da seguinte maneira:

# print(f"O número 1 apareceu {cont1} vezes\n"
#       f"O número 2 apareceu {cont2} vezes\n"
#       f"O número 3 apareceu {cont3} vezes\n"
#       f"O número 4 apareceu {cont4} vezes\n"
#       f"O número 5 apareceu {cont5} vezes\n"
#       f"O número 6 apareceu {cont6} vezes")

#Mesmo estando em linhas diferentes, ele ainda printaria como se estivesse em uma única linha
#Logo os \n ainda são necessários ali.

print(f"O número 1 apareceu {cont1} vezes\nO número 2 apareceu {cont2} vezes\nO número 3 apareceu {cont3} vezes\nO número 4 apareceu {cont4} vezes\nO número 5 apareceu {cont5} vezes\nO número 6 apareceu {cont6} vezes")

#Boa abordagem para este exercício! O uso da biblioteca Random é essencial! Boa!