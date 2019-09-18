#Gabriel Costa Kinder - 234720

def main():
    ord = 'n'  # variavel para ordenacao, n = sem ordenacao, c = crescente, d = decrescente
    alunos = input().split()  # obtem numeros de ras
    alunos = [int(i) for i in alunos]  # transforma todos em int
    while True:  # loop infinito ate ser digitado 's'
        aux = input().split()  # obtem comando desejado
        if aux[0] == 's':  # se for digitado 's' sai do loop e finaliza o programa
            break
        elif aux[0] == 'p':  # se for digitado 'p' chama funcao para imprimir lista de ras
            printalunos(alunos)
        elif aux[0] == 'c':  # se for digitado 'c' chama funcao para ordenar de forma crescente e muda a variavel ord para 'c'
            ord = 'c'
            ordemc(alunos)
        elif aux[0] == 'd':  # se for digitado 'd' chama funcao para ordenar de forma decrescente e muda a variavel ord para 'd'
            ord = 'd'
            ordemd(alunos)
        elif aux[0] == 'b':  # se for digitado 'b' chama funcao para busca binaria em busca de ra digitado
            buscabin(alunos, ord, int(aux[1]))
        elif aux[0] == 'i':  # se for digitado 'i' chama funcao para inserir corretamente um valor de ra na ordem correta
            insertaluno(alunos, ord, int(aux[1]))
        elif aux[0] == 'r':  # se for digitado 'r' chama funcao para remover o valor digitado
            removealuno(alunos, int(aux[1]))

def printalunos(alunos):
    if len(alunos) == 0:  # caso nao haja ras, n faz nada
        return
    for i in alunos:
        print(i, end=" ")  # printa o valor de cada ra em uma unica linha com um " " entre cada ra
    print("")  # passa de linha


def ordemc(alunos):
    for j in range(len(alunos)):  # repete len(alunos) vezes
        for i in range(len(alunos)-1):  # assume os valores que serao testados e movidos
            if alunos[i] > alunos[i+1]:  # se o valor anterior for maior que o superior, troca ambos de lugar
                alunos[i], alunos[i+1] = alunos[i+1], alunos[i]


def ordemd(alunos):  # analoga a funcao anterior, porem faz a troca se o valor for menor
    for j in range(len(alunos)):
        for i in range(len(alunos)-1):
            if alunos[i] < alunos[i+1]:
                alunos[i], alunos[i+1] = alunos[i+1], alunos[i]


def buscabin(alunos, ord, ra):
    if ord == 'n':  # caso nao haja ordenacao, imprime erro e retorna
        print("Vetor nao ordenado!")
        return
    ini = 0  # assume valores de inicio e fim para a busca binaria
    fim = len(alunos)-1
    if ord == 'c':  # se a ordem for crescente
        while True:  # loop de busca binaria
            meio = (ini + fim)//2  # assume valor do meio como a divisao truncada por 2 de inicio + fim
            print (meio, end=" ")  # printa valor do indice sendo utilizado
            if alunos[meio] == ra:  # caso o valor do ra procurado esteja no indice meio, imprime a seguinte mensagem com o ra + posicao e retorna
                print("\n%d esta na posicao: %d"%(ra, meio))
                return
            if alunos[meio] > ra:  # caso valor do ra seja maior, admite um novo valor para fim
                fim = meio - 1
            if alunos[meio] < ra:  # caso valor do ra seja menor, admite um novo valor para ini
                ini = meio + 1
            if fim == meio or ini == meio:  # caso ja tenha-se terminado a busca e nao encontrado o valor desejado, imprime a seguinte mensagem e retorna
                print("\n%d nao esta na lista!"%(ra))
                return
    if ord == 'd':  # analoga a funcao anterior porem considerando a ordenacao decrescente
        while True:
            meio = (ini + fim)//2
            print (meio, end=" ")
            if alunos[meio] == ra:
                print("\n%d esta na posicao: %d"%(ra, meio))
                return
            if alunos[meio] < ra:
                fim = meio - 1
            if alunos[meio] > ra:
                ini = meio + 1
            if fim == meio or ini == meio:
                print("\n%d nao esta na lista!"%(ra))
                return


def insertaluno(alunos, ord, ra):
    if len(alunos) >= 150:  # mensagem de erro caso a lista ja possua o numero maximo de ras permitido e retorna
        print("Limite de vagas excedido!")
        return
    if ra in alunos:  # caso ra ja esteja na turma imprime a mensagem e retorna
        print("Aluno ja matriculado na turma!")
        return
    if ord == 'n':  # caso nao haja ordenacao na lista, coloca valor de ra na ultima posicao e retorna
        alunos.append(ra)
        return
    if ord == 'c':  # caso haja ordenacao crescente:
        if alunos[-1] < ra:  # testa se o ra deve ser inserido na ultima posicao
            alunos.append(ra)
        if alunos[0] > ra:  # testa se o ra deve ser inserida na primeira posicao
            alunos.insert(0, ra)
        for i in range(len(alunos)-1):
            if ra > alunos[i] and ra < alunos[i+1]:  # verifica cada posicao e os ras ao seu redor, caso o ra a ser inserido esteja entre eles, o insere e retorna
                alunos.insert(i+1, ra)
                return
    if ord == 'd':  # analoga a ultima, porem com ordenacao decrescente
        if alunos[-1] > ra:
            alunos.append(ra)
        if alunos[0] < ra:
            alunos.insert(0, ra)
        for i in range(len(alunos)-1):
            if ra < alunos[i] and ra > alunos[i+1]:
                alunos.insert(i+1, ra)
                return


def removealuno(alunos, ra):
    if len(alunos) == 0:  # mensagem caso nao haja alunos na turma
        print("Nao ha alunos cadastrados na turma!")
    elif ra in alunos:  # se o ra a ser removido esta na lista, o remove
        alunos.remove(ra)
    else:  # caso nao esteja, da uma mensagem de erro
        print("Aluno nao matriculado na turma!")


main()
