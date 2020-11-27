####################################################################################################### 

# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 

#######################################################################################################

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

#Esta condição só funciona se o lado1 foi o maior lado.
#Você pode resolver isso adicionando as outras condições (lado2 >= lado1 + lado3...)
#Ou você pode organizar os inputs para que o lado1 seja sempre o maior lado.
#Ex:
#lado1 = 2
#lado2 = 30
#lado3 = 1
#Resultado = "Triângulo escaleno"
#porém estas dimensões não formam triângulo.
if (lado1 >= lado2 + lado3):
    print("Não forma triângulo")
else:
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo equilátero")
    
    #Nesta condição abaixo, não é necessário falar que ladoX != ladoY, pois na condição anterior ele já verifica se são todos iguais
    #Não é errado deixar bem claro a condição que você quer, porém é possível fazer uma comparação apenas se 2 dos lados são iguais
    elif lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado2 != lado1 or lado1 == lado3 and lado1 != lado2:
        print("Triângulo isósceles")
    elif lado1 != lado2 and lado1 != lado3:
        print("Triângulo escaleno")

#Organização do código (antes de eu bagunçar) está muito boa.
#Apenas se atentar às validações. De resto está show!