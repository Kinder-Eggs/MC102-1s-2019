# Gabriel Costa Kinder - 234720
iter = 0  # contador de numero de iteracoes

def main():
    tam = input().split()  # adquire tamanho da matriz
    tam[0] = int(tam[0])  # converte para int
    tam[1] = int(tam[1])
    dias = int(input())  # adquire numero de dias
    matriz = [[0 for i in range(tam[1]+2)] for j in range(tam[0]+2)]  # gera matriz i+2,j+2 preenchida com 0
    for x in range(tam[0]):
        linha = input()
        aux = [int(i) for i in linha.split()]  # preenche umaa matriz com os valores lidos
        i = 0
        while i < len(aux):  # preence a matriz final linha por linha
            matriz[x+1][i+1] = aux[i]
            i += 1
    printmatriz(matriz)  # chama a funcao para imprimir a matriz
    i = 0
    while i < dias:  # realiza o teste para o numero de dias necessarios
        matriz = proxdia(matriz)  # chama a funcao que calcula o que ocorrera no dia seguinte
        printmatriz(matriz)  # printa matriz
        i += 1


def printmatriz(matriz):  # definicao para printar a matriz
    global iter
    print ("iteracao", iter)  # printa numero do dia do teste
# sequencia de comandos para imprimir a matriz da forma desejada
    for i in range(1, len(matriz) - 1):
        for j in range(1, len(matriz[0]) - 1):
            print (matriz[i][j], end="")
        print("")
    iter += 1  # aumenta numero de iteracoes realizadas em 1


def proxdia(matriz):  # verifica como estara a matriz no dia seguinte
    matrizaux = [[matriz[i][j] for j in range(len(matriz[0])) ] for i in range(len(matriz))]  # cria uma copia numerica da matriz original em matrizaux

    for i in range(1, len(matriz) - 1):
        for j in range(1, len(matriz[0]) - 1):
            h = 0  # variaveis para contage de humanos e zumbis
            z = 0
            x = matriz[i][j]  # verifica o que ocupa o espaco que esta sendo verificado

# realiza a contagem de humanos e zumbis ao redor de um determinado ponto
            if matriz[i-1][j-1] == 2:
                z += 1
            elif matriz[i-1][j-1] == 1:
                h += 1
            if matriz[i-1][j] == 2:
                z += 1
            elif matriz[i-1][j] == 1:
                h += 1
            if matriz[i-1][j+1] == 2:
                z += 1
            elif matriz[i-1][j+1] == 1:
                h += 1
            if matriz[i][j-1] == 2:
                z += 1
            elif matriz[i][j-1] == 1:
                h += 1
            if matriz[i][j+1] == 2:
                z += 1
            elif matriz[i][j+1] == 1:
                h += 1
            if matriz[i+1][j-1] == 2:
                z += 1
            elif matriz[i+1][j-1] == 1:
                h += 1
            if matriz[i+1][j] == 2:
                z += 1
            elif matriz[i+1][j] == 1:
                h += 1
            if matriz[i+1][j+1] == 2:
                z += 1
            elif matriz[i+1][j+1] == 1:
                h += 1

# dependendo do valor de humanos e zumbis ao redor de determinado ponto e o que ocupa este determinado ponto, coloca o que o ocupara no dia seguinte
            if x == 1 and z > 0:
                matrizaux[i][j] = 2
            elif x == 2:
                if h > 1 or h == 0:
                    matrizaux[i][j] = 0
            elif x == 0 and h == 2:
                matrizaux[i][j] = 1

    return matrizaux  # retorna a matriz com os valores do dia seguinte


main()
