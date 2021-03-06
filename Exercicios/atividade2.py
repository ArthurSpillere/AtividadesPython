######################################################################################################

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# 

#######################################################################################################

def apenas18(litros):
    cont = 0
    while litros > 0:
        litros -= 18
        cont += 1
    return cont
#Muito interessante a ideia de fazer um contador dentro de um While para saber a quantidade de latas necessárias
#Outro jeito de se fazer é usando divisão inteira (//) e resto da divisão (%)
#A divisão inteira retorna o total de latas e se houver resto, adicionar uma lata extra.

def apenas36(litros):
    cont = 0
    while litros > 0:
        litros -= 3.6
        cont += 1
    return cont

def misturado(litros):
    cont18 = 0
    cont36 = 0
    lista = []
    while litros > 0:
        if litros >= 18:
            litros -= 18
            cont18 += 1
        elif litros < 18:
            litros -= 3.6
            cont36 += 1
    lista.append(cont18)
    lista.append(cont36)
    return(lista)

metros = float(input("Tamanho em metros da parede a ser pintada: "))
#Como eu apanhei na engenharia por isso, vou comentar aqui também hahaha
#Se atente às unidades de medida. O certo é "metros quadrados" ou "m²".

litrosNecessarios = metros / 6 # Regra de 3
#Aqui faltou multiplicar o valor de litros necessários por 1.1 (10% a mais)
#Conforme foi pedido na questão.

if __name__ == "__main__":
    while True:
        escolha = int(input("""
1. Resultado apenas com latas 18 litros
2. Resultado apenas com latas 3,6 litros
3. Resultado misturado
0. Sair
"""))

#Mesma coisa com a unidade de medida aqui também.
        if escolha == 1:
            print(f"Para pintar {metros:.2f} metros será necessário {apenas18(litrosNecessarios)} galão(es) de 18 litros")
        elif escolha == 2:
            print(f"Para pintar {metros:.2f} metros será necessário {apenas36(litrosNecessarios)} galão(es) de 3,6 litros")
        elif escolha == 3:
            print(f"Para pintar {metros:.2f} metros será necessário {misturado(litrosNecessarios)[0]} galão(es) de 18 litros e {misturado(litrosNecessarios)[1]} lata(s) de 3,6 litros")
        elif escolha == 0:
            print("Até mais.")
            break

#No geral muito bom o código. Gostei da clareza e de como você pensou
#para resolver ela. Show!