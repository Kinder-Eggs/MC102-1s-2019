#!/usr/bin/env python3

import math

# Laboratorio 17 - Banco de Dados Geografico
# Nome: Gabriel Costa Kinder
# RA: 234720

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cidade:
    def __init__(self, coordenadas, inicioCEP, fimCEP, numHabitantes):
        self.coordenadas = coordenadas
        self.inicioCEP = inicioCEP
        self.fimCEP = fimCEP
        self.numHabitantes = numHabitantes

#
# Funcao: distancia
#
# Parametros:
#   a, b: pontos
#
# Retorno:
#   A distancia euclidiana entre a e b.
#
def distancia(c1, c2):
    return int(100 * math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)) / 100.0

# Funcao: consulta_cidade_por_cep
#
# Parametros:
#   cidades: lista de cidades (base de dados)
#       cep: CEP desejado
#
# Retorno:
#   O indice da cidade que contem o CEP desejado ou None caso não haja tal cidade.
#
def consulta_cidade_por_cep(cidades, cep):
    for i in range(len(cidades)):
        if cidades[i].fimCEP > cep > cidades[i].inicioCEP:  # testa entre cada cidade no banco de dados se o CEP buscado esta entre os ceps extremos daquela cidade
            return i  # retorna cidade onde foi encontrado
    return None  # se nao for encontrado retorna None

# Funcao: consulta_cidades_por_raio
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Lista dos indices das cidades que estao contidas no raio de busca (incluindo
#   a cidade referencia) *ordenados pelas respectivas distancias da cidade referencia*.
#
def consulta_cidades_por_raio(cidades, cidadeReferencia, raio):
    results = []  # cria uma lista vazia para conter os resultados
    for i in range(len(cidades)):  # testa, para cada cidade, se a distance entre ela e a cidadeReferencia corresponde ao reio desejado
        if distancia(cidades[cidadeReferencia].coordenadas, cidades[i].coordenadas) < raio:
            results.append(i)  # se sim, da append em seu indice na lista de resultados
    if len(results) == 0:  # caso nao haja nenhum indice em resultados, retorna None
        return None
    for i in range(len(results)):  # realiza um algoritmo de sorting com base nas distancias para organizar com as cidades mais proximas primeiro e as cidades mais longes por ultimo
        for j in range(len(results)-1):
            if distancia(cidades[results[j]].coordenadas, cidades[cidadeReferencia].coordenadas) > distancia(cidades[results[j+1]].coordenadas, cidades[cidadeReferencia].coordenadas):
                results[j], results[j+1] = results[j+1], results[j]
    return results  # retorna a lista com os resultados ordenados

# Funcao: populacao_total
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   O numero de habitantes das cidades que estao contidas no raio de busca
#
def populacao_total(cidades, cidadeReferencia, raio):
    poptotal = 0  # cria uma variavel para conter a populacao total
    inradius = consulta_cidades_por_raio(cidades, cidadeReferencia, raio)  # adiciona todas as cidades no raio requerido em uma lista inradius utilizando a funcao de consulta_cidades_por_raio
    for i in inradius:
        poptotal += cidades[i].numHabitantes  # soma a populacao de cada cidade em poptotal
    if poptotal == 0:  # caso nao haja cidade, retorna None
        return None
    return poptotal  # retorna poptotal

# Funcao: mediana_da_populacao
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Mediana do numero de habitantes das cidades que estao contidas no raio de busca
#
def mediana_da_populacao(cidades, cidadeReferencia, raio):
    poplist = []  # cria uma lista vazia que ira conter o valor de populacao de cada cidade
    inradius = consulta_cidades_por_raio(cidades, cidadeReferencia, raio)  # adiciona cidades dentro do raio requerido
    for i in inradius:
        poplist.append(cidades[i].numHabitantes)  # adiciona valor de cada populacao em poplist
    if poplist == 0:  # caso nao haja cidades retorna None
        return None
    poplist.sort()  # organiza poplist em ordem crescente
    if (len(poplist) % 2) == 1:  # caso a divisao de poplist por 2 tenha resto 1 (considerando que poplist comeca em 0 isso significa que ha um numero par de cidades)
        return poplist[(len(poplist)//2)]  # retorna o valor no meio de poplist
    else:
        return (poplist[int(len(poplist)/2)] + poplist[int(len(poplist)/2)-1])/2  # caso houver um numero impar de populacoes, soma os dois termos no meio, divide por 2, e retorna este valor
