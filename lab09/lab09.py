#Gabriel Kinder - 234720

i = 1  # variavel para loop while
N = int(input())  # Le tamanho NxN da matriz
matfin = []  # Cria a matriz final vazia
cont = 0  # variavel contadora para numero de divisores

def verMult(i, j): #Funcao que verifica divisor
    if i > j:  # se i > j divide i por j
        if i%j == 0:  # se resto igual a 0 retorna verdadeiro (é divisor)
            return True
    elif j > i:  # se j > i divide j por i
        if j%i == 0:
            return True
    else:  # quando i==j, sao divisores, retorna True
        return True
    return False  # quando nada retorna True, retorna False (não é divisor)


while (i-1 < N):  # loop while para gerar matriz
    mataux = []  # cria matriz auxiliar(se transforma em linhas na matriz final)
    j = 1  # variavel para loop while
    while (j-1 < N):
        divisor = verMult(i, j)  # chama função para verificar divisão de i e j
        if divisor == True:  # se divide adiciona * na matriz auxiliar
            mataux.append("*")
            cont += 1  # soma 1 no contador de divisores
        else:  # se não divide adiciona -
            mataux.append("-")
        j += 1
    matfin.append(mataux)  # adiciona a matriz auxiliar na matriz final
    i += 1

i = 0  # variaveis para loop while
while i < N:
    j = 0
    while j < N:
        print (matfin[i][j], end="")  # printa * ou - na mesma linha
        j += 1
    print("")  # pula para a prox linha
    i += 1
print(cont)  # printa variavel contadora
