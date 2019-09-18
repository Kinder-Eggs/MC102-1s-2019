# Gabriel Costa Kinder - 234720


def updatedatabase(data, database):  # atualiza database
    for j in range(152):  # verifica se ja existe dados para este I
        if int(data[0]) == database[j][1]:  # caso haja, soma os valores no BC antigo, soma 1 no cont e retorna a main
            database[j][0] += int(data[2]) / int(data[1])
            database[j][2] += 1
            return
    for x in range(152):  # caso nao haja, verifica primeiro indice nao ocupado e o ocupa
        if database[x][1] == 0:
            database[x][1] = int(data[0])
            database[x][0] += int(data[2]) / int(data[1])
            database[x][2] += 1
            return


def calculatemultipliers(database):  # calcula multiplicadores de evolucao
    for j in range(152):
        if database[j][2] != 0:  # evita divisao por zero
            database[j][0] = database[j][0]/database[j][2]  # calcula a media dos multiplicadores


def testevolutions(database):  # calcula PCf das proximas evolucoes ate valor 0 0 ser dado como entrada
    while True:  # repete ate atingir o return
        aux = input().split()  # obtem I e PCa do monstro para teste e salva em aux
        aux[0] = int(aux[0])  # converte valores para int
        aux[1] = int(aux[1])
        if aux[0] == 0 and aux[1] == 0:  # caso valor digitado seja 0 0 finaliza o programa
            return
        for j in range(152):  # verifica onde estao os dados para dado indice
            if aux[0] == database[j][1]:
                print(int(database[j][0] * aux[1]) + 1)  # printa PCf esperado
                break


def main():  # funcao principal
    database = []  # cria lista vazia (futuro banco de dados)
    N = int(input())  # numero de evolucoes que serao dadas
    i = 0
# Cria uma lista de banco de dados com valor de M no indice 0, I no indice 1 e um contador no indice 2
    while i < 152:
        database.append([0, 0, 0])
        i += 1
    while N > 0:  # atualiza o banco de dados N vezes
        data = input().split()  # obtem 3 valores (I, PCa e PCf) e salva em uma lista chamada "data"
        updatedatabase(data, database)  # envia data e o banco de dados para atualizar
        N -= 1
    calculatemultipliers(database)
    testevolutions(database)


main()
