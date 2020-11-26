#######################################################################################################

# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u. 


########################################################################################################

contEspaco = 0
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0

frase = input("Digite sua frase: ")

for caracter in frase:
    if ord(caracter) == 32:
        contEspaco += 1
    elif ord(caracter) == 65 or ord(caracter) == 97:
        contA += 1
    elif ord(caracter) == 69 or ord(caracter) == 101:
        contE += 1
    elif ord(caracter) == 73 or ord(caracter) == 105:
        contI += 1
    elif ord(caracter) == 79 or ord(caracter) == 111:
        contO += 1
    elif ord(caracter) == 85 or ord(caracter) == 117:
        contU += 1

print(f"A frase possui {contEspaco} espaços, {contA} letras A(a), {contE} letras E(e), {contI} letras I(i), {contO} letras O(o), {contU} letras U(u).")
    