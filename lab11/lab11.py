# Gabriel Costa Kinder - 234720
def main():
    dias = int(input())  # armazena a quantia de dias
    lucros = []  # cria listas vazias para armazenar lucros e dados
    data = []
    data = gerardata(data, dias)  # chama a funcao que preenche a lista de dados
    lucros = gerarlucros(lucros, dias)  # gera uma lista de lucros vazia que possui uma lista para cada dia - 1 com 4 valores (1 para cada empresa)
    lucros = calcularlucros(lucros, dias, data)  # preenche a lista com as mudancas nos valores das acoes de cada empresa, indice 0 sendo a diferenca entre o dia 1 e dia 2 e assim por diante
    maxlucro = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # cria uma lista com 13 variaveis que serao preenchidas posteriormente referentes ao cenario com maior lucro
    for c1 in range(dias):  # comeco dos 8 loops fors para testar cada possibilidade, onde cx eh a data da compra da empresa x, vx a data da venda e lx o Lucro de tal combinacao.
        for v1 in range(dias):
            if v1 < c1:  # evita datas de venda anteriores as de compra
                continue  # caso seja, passa para a proxima combinacao
            l1 = 0  # zera o lucro 1 para cada combinacao com valor diferente para c1 e v1
            i = 0
            while i < v1-c1:  # calcula o lucro 1 para a atual combinacao
                l1 += lucros[c1+i][0]
                i += 1
            for c2 in range(dias):
                if c2 == c1 and l1 != 0:  # evita datas de compras iguais, exceto quando nao houve compra para a anterior (c1==v1, logo l1=0)
                    continue
                for v2 in range(dias):
                    if v2 < c2:
                        continue
                    l2 = 0
                    i = 0
                    while i < v2-c2:
                        l2 += lucros[c2+i][1]
                        i += 1
                    for c3 in range(dias):
                        if c3 == c1 and l1 != 0 or c3 == c2 and l2 != 0:
                            continue
                        for v3 in range(dias):
                            if v3 < c3:
                                continue
                            l3 = 0
                            i = 0
                            while i < v3-c3:
                                l3 += lucros[c3+i][2]
                                i += 1
                            for c4 in range(dias):
                                if c4 == c3 and l3 != 0 or c4 == c2 and l2 != 0 or c4 == c1 and l1 != 0:
                                    continue
                                for v4 in range(dias):
                                    if v4 < c4:
                                        continue
                                    if v2 > c1 > c2 or v3 > c1 > c3 or v4 > c1 > c4 or v1 > c2 > c1 or v3 > c2 > c3 or v4 > c2 > c4 or v1 > c3 > c1 or v2 > c3 > c2 or v4 > c3 > c4 or v1 > c4 > c1 or v2 > c4 > c2 or v3 > c4 > c3:  # evita datas de compras que ocorrem ao ja se possuir uma outra acao comprada
                                        continue
                                    if v2 > v1 > c2 or v3 > v1 > c3 or v4 > v1 > c4 or v1 > v2 > c1 or v3 > v2 > c3 or v4 > v2 > c4 or v1 > v3 > c1 or v2 > v3 > c2 or v4 > v3 > c4 or v1 > v4 > c1 or v2 > v4 > c2 or v3 > v4 > c3:  # evita datas de venda que ocorrem apenas ao ja se ter comprado outra acao
                                        continue
                                    l4 = 0
                                    i = 0
                                    while i < v4-c4:
                                        l4 += lucros[c4+i][3]
                                        i += 1
                                    if l1+l2+l3+l4 > maxlucro[0]:  # caso nova combinacao tenha maior lucro que a anterior, preenche maxlucro com todos os dados [lt, c1, v1, l1, c2, v2, l2, c3, v3, l3, c4, v4, l4]
                                        maxlucro[0] = l1+l2+l3+l4
                                        maxlucro[1] = c1+1  # adiciona 1 para todos os cxs e vxs pois, como listas comecao no indice 0, a data real eh um numero maior
                                        maxlucro[2] = v1+1
                                        maxlucro[3] = l1
                                        maxlucro[4] = c2+1
                                        maxlucro[5] = v2+1
                                        maxlucro[6] = l2
                                        maxlucro[7] = c3+1
                                        maxlucro[8] = v3+1
                                        maxlucro[9] = l3
                                        maxlucro[10] = c4+1
                                        maxlucro[11] = v4+1
                                        maxlucro[12] = l4
    printcompras(maxlucro)  # chama funcao que imprime na tela o resultado de maior lucro

def gerardata(data, dias):
    j = 0
    while j < 4:  # loop para gerar a lista auxiliar
        aux = []
        i = 0
        while i < dias:
            aux.append(float(input()))  # armazena as informacoes sendo enviadas na lista auxiliar para cada dia
            i += 1
        j += 1
        data.append(aux)  # adiciona a lista auxiliar no lista de dados, totalizando em 4 listas (uma por empresa) com os valores das acoes de cada dia
    return data  # retorna a lista contendo os dados


def gerarlucros(lucros, dias):
    j = 0
    while j < dias-1:
        lucros.append([0, 0, 0, 0])  # adiciona uma lista de 4 valores para cada dia - 1
        j += 1
    return lucros


def calcularlucros(lucros, dias, data):
        d = 0
        e = 0
        for d in range(dias-1):
            for e in range(4):
                lucros[d][e] = data[e][d+1] - data[e][d]  # subtrai o dia anterior para obter as diferencas nos valores das acoes (lucros e prejuizos)
        return lucros


def printcompras(maxlucro):
    if maxlucro[3] != 0:  # verifica se houve compra e venda de acoes das empresas (l != 0), somente imprime caso haja
        print("acao 1: compra %d, venda %d, lucro %.2f" % (maxlucro[1], maxlucro[2], maxlucro[3]))  # printa data da compra, data da venda, e lucro obtido com tal
    if maxlucro[6] != 0:
        print("acao 2: compra %d, venda %d, lucro %.2f" % (maxlucro[4], maxlucro[5], maxlucro[6]))
    if maxlucro[9] != 0:
        print("acao 3: compra %d, venda %d, lucro %.2f" % (maxlucro[7], maxlucro[8], maxlucro[9]))
    if maxlucro[12] != 0:
        print("acao 4: compra %d, venda %d, lucro %.2f" % (maxlucro[10], maxlucro[11], maxlucro[12]))
    print("Lucro: %.2f" % (maxlucro[0]))  # printa lucro total obtido

main()  # chama funcao principal
