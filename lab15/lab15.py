#!/usr/bin/env python3
#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
    jogo = jogo.split()
    #  jogo[0] = time1 | jogo[1] = gols time 1 | jogo[2] = 'X' | jogo[3] = gols time 2 | jogo[4] = time2
    if jogo[1] > jogo[3]:  # descobre time vencedor
        aux = 1
    elif jogo[1] < jogo[3]:
        aux = 2
    else:  # caso empate
        aux = 0
    for i in range(len(tabela)):  # adiciona saldo de gols e gols pros para ambos os times, alem dos pontos baseado na variavel aux (quem venceu)
        if tabela[i][0] == jogo[0]:  # se posicao i na tabela se refere ao time 1:
            tabela[i][4] += int(jogo[1])
            tabela[i][3] += (int(jogo[1]) - int(jogo[3]))
            if aux == 1:
                tabela[i][1] += 3
                tabela[i][2] += 1
            if aux == 0:
                tabela[i][1] += 1
        if tabela[i][0] == jogo[4]:  # se posicao i na tabela se refere ao time 2:
            tabela[i][4] += int(jogo[3])
            tabela[i][3] += (int(jogo[3]) - int(jogo[1]))
            if aux == 2:
                tabela[i][1] += 3
                tabela[i][2] += 1
            if aux == 0:
                tabela[i][1] += 1
#*******************************************************************************

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
    if time1[1] > time2[1]:  # caso time 1 tenha mais pontos retorna 1
        return 1
    if time1[1] == time2[1]:  # se for igual testa o prox
        if time1[2] > time2[2]:  # se num de vitorias maior retorna 1
            return 1
        if time1[2] == time2[2]:  # se for igual testa o prox
            if time1[3] > time2[3]:  # se saldo de gols maior retorna 1
                return 1
            if time1[3] == time2[3]:  # se for igual testa o prox
                if time1[4] > time2[4]:  # se gols pros maior retorna 1
                    return 1
                if time1[4] == time2[4]:  # se for igual retorna 0
                    return 0
    return -1  # se nenhum retorno for atingido time2 > time 1, portanto retorna -1
#*******************************************************************************


#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
    for i in range(len(tabela)):  # loop len(tabela) vezes
        for j in range(len(tabela) - (i + 1)):  # testa todos os valores necessarios para a ordenacao
            aux = comparaTimes(tabela[j], tabela[j+1])  # obtem o vencedor entre dois jogadores
            if aux == -1:  # caso time2 > time1, inverte a posicao de ambos na tabela
                tabela[j], tabela[j+1] = tabela[j+1], tabela[j]
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************


#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
    for i in tabela:  # repete para cada jogador
        for j in range(len(i) - 1):  # repete len(i)-1 vezes para imprimir todos os valores menos o ultimo
            print(str(i[j]) + ',', end=" ")  # imprime um valor, adiciona uma virgula apos ele e nao pula a linha
        print(i[-1])  # adiciona o valor restante deste time e pula a linha para o proximo time
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
