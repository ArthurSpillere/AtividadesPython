#######################################################################################################

# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e 
# no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, 
# com números de 1 a 9:

#     8  3  4 
#     1  5  9
#     6  7  2

# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. 

#######################################################################################################

# [0][0] [0][1] [0][2]
# [1][0] [1][1] [1][2]
# [2][0] [2][1] [2][2]

import random

quadradoMagico = [0, 0, 0, 0, 0, 0, 0, 0, 0]
quadradoMagico[4] = 5
possibilidades = 8
ordemSorteioImpar = []
ordemSorteioPar = []

def geradorNumerosImpares():
    impar = [1, 3, 7, 9]
    random.shuffle(impar)
    if impar in ordemSorteioImpar:
        while impar in ordemSorteioImpar:
            #Faltou parenteses aqui pra chamar a função()
            geradorNumerosImpares
    else:
        quadradoMagico[1] = impar[0]
        quadradoMagico[3] = impar[1]
        quadradoMagico[5] = impar[2]
        quadradoMagico[7] = impar[3]
        ordemSorteioImpar.append(impar[0])
        ordemSorteioImpar.append(impar[1])
        ordemSorteioImpar.append(impar[2])
        ordemSorteioImpar.append(impar[3])

def geradorNumerosPares():
    par = [2, 4, 6, 8]
    random.shuffle(par)
    if par in ordemSorteioPar:
        while par in ordemSorteioPar:
            geradorNumerosPares()
    else:
        quadradoMagico[0] = par[0]
        quadradoMagico[2] = par[1]
        quadradoMagico[6] = par[2]
        quadradoMagico[8] = par[3]
        ordemSorteioPar.append(par[0])
        ordemSorteioPar.append(par[1])
        ordemSorteioPar.append(par[2])
        ordemSorteioPar.append(par[3])

while (possibilidades > 0):
    geradorNumerosImpares()
    geradorNumerosPares()
    #Vou ser sincero que me perdi nessa linha sem fim ali embaixo hahahaha
    #como vimos nas boas práticas ontem e hoje, pode-se dividir cada condição e armazenar ela em uma variável e colocar no if
    #Ou você pode fazer quebras de linhas em cada condição:
    
    # if (quadradoMagico[0] + quadradoMagico[1] + quadradoMagico[2] == 15
    #     and quadradoMagico[3] + quadradoMagico[4] + quadradoMagico[5] == 15
    #     and quadradoMagico[6] + quadradoMagico[7] + quadradoMagico[8] == 15
    #     and quadradoMagico[0] + quadradoMagico[3] + quadradoMagico[6] == 15
    #     and quadradoMagico[1] + quadradoMagico[4] + quadradoMagico[7] == 15
    #     and quadradoMagico[2] + quadradoMagico[5] + quadradoMagico[8] == 15
    #     and quadradoMagico[0] + quadradoMagico[4] + quadradoMagico[8] == 15
    #     and quadradoMagico[2] + quadradoMagico[4] + quadradoMagico[6] == 15):
    
    if quadradoMagico[0] + quadradoMagico[1] + quadradoMagico[2] == 15 and quadradoMagico[3] + quadradoMagico[4] + quadradoMagico[5] == 15 and quadradoMagico[6] + quadradoMagico[7] + quadradoMagico[8] == 15 and quadradoMagico[0] + quadradoMagico[3] + quadradoMagico[6] == 15 and quadradoMagico[1] + quadradoMagico[4] + quadradoMagico[7] == 15 and quadradoMagico[2] + quadradoMagico[5] + quadradoMagico[8] == 15 and quadradoMagico[0] + quadradoMagico[4] + quadradoMagico[8] == 15 and quadradoMagico[2] + quadradoMagico[4] + quadradoMagico[6] == 15:
        print("\n###")
        print(quadradoMagico[0], quadradoMagico[1], quadradoMagico[2])
        print(quadradoMagico[3], quadradoMagico[4], quadradoMagico[5])
        print(quadradoMagico[6], quadradoMagico[7], quadradoMagico[8])
        print("###\n")
        #print(todos)
        possibilidades -= 1

        print(ordemSorteioPar)
        print(ordemSorteioImpar)


#Entendi o código. Bacana o jeito de se pensar. Parte do princípio que você já sabe que 
#há apenas 8 possibilidades e que o 5 precisa estar no meio para funcionar.
#Creio que você está sim no caminho, apenas seria necessário armazenar as linhas que deram certo
#e comparar se esta possibilidade já foi printada antes de subtrair do contador "possibilidades"
#Gostei das tuas variáveis.. preciso aprender contigo como ter variáveis explícitas e ainda assim ter
#um código bonito! Muito bom!

#import random
#
##par = [2, 4, 6, 8]
#impar = [1, 3, 5, 7, 9]

#
#def geradorNumerosImpares():
#    print(impar)
#    a = random.shuffle(impar)
#    print(a)
#
#def geradorNumerosPares():
#    listaPares = sorted(random.sample(range(2, 10, 2), 4))
#    print(listaPares)
#
##for num in quadradoMagico:
##    quadradoMagico[num][num] = par[num]
#
#geradorNumerosImpares()
#geradorNumerosPares()