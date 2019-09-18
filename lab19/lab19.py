#Gabriel Costa Kinder - 234720

import random

def main():
    resultado = []  # cria uma lista que contera os valores dos subordinados
    nk = input().split()  # obtem valor de n (numero de funcionarios) e de k (funcionario desejado a se obter a hierarquia)
    hier = []  # lista onde sera contido a matriz de hierarquia geral passada como entrada
    for i in range(int(nk[0])):
        hier.append(input().split())

    print(nk[1], end="")  # printa o funcionario desejada, sem pular linha
    get_hier(hier, int(nk[1]), resultado)  # chama uma funcao recursiva que ira adicionar os funcionarios subordinados a k na lista resultado
    if len(resultado):  # caso exista algo em resultado (k possui funcionarios subordinados)
        quicksort(resultado, 0, len(resultado)-1)  # executa quicksort em resultados
        print(" ", end="")  # adiciona um espaco em branco apos k
        for i in range(len(resultado)-1):  # imprime em ordem crescente cada um dos funcionarios subordinados a k (exceto o ultimo) com um espaco no final
            print(resultado[i], end=" ")
        print(resultado[-1])  # imprime o ultimo funcionario subordinado sem o espaco no final
    else:  # caso nao haja funcionarios subordinados a k pula a linha
        print()


def get_hier(hier, k, resultado):  # funcao recursiva para obter os funcionarios subordinados
    for i in range(len(hier[k])):  # itera sob a linha correspondente ao funcionario k
        if hier[k][i] == '1':  # caso encontre algum valor 1 adiciona-o a resultado e chama a funcao novamente em busca dos funcionarios subordinados a este subordinado
            resultado.append(i)
            get_hier(hier, i, resultado)


def quicksort(lista, inicio, fim):  # executa um quicksort recursivo em lista com inicio em inicio e fim em fim
    if (inicio < fim):
        #j = random.randint(inicio, fim)
        #lista[j], lista[fim] = lista[fim], lista[j]
        part = particiona(lista, inicio, fim)  # particiona a lista
        quicksort(lista, inicio, part-1)  # executa o quicksort em ambas as partes
        quicksort(lista, part, fim)


def particiona(lista, inicio, fim):
    pivot = lista[fim]  # escolhe ultimo valor como pivot
    while inicio < fim:  # encontra valores maiores e menores que pivot para alterar a ordem de lista
        while (inicio < fim) and (lista[inicio] <= pivot):
            inicio += 1
        while (inicio < fim) and (lista[fim] > pivot):
            fim += -1
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
    return inicio  # retorna valor de inicio


main()
