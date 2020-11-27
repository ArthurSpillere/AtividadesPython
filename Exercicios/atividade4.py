#######################################################################################################

# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário. 

#######################################################################################################

numLimite = int(input("Digite um número: "))

for i in range(1, numLimite + 1):
    cont = 0
    for j in range(1, numLimite + 1):
        if i % j == 0:
            cont += 1
    if (cont == 2):
        print(i)

#Gostei da ideia! Para otimizar eu sugiro colocar uma condição
#pra quando j > (i/2) ele pular para o próximo i e adicionar o i como primo.
#A lógico é a seguinte:
#Ex. i = 71
#Se j estiver em 35 e ainda não tem cont = 2, ele já pode ser considerado primo,
#pois não terá mais nenhuma divisão inteira após o 35. 
#Isso deve ajudar o código a não ter que dividir todos os números por todos os números
#Espero ter sido claro hahaha.
#Bom trabalho!