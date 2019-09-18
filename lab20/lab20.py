#!/usr/bin/env python3

#Gabriel Costa Kinder - 234720

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku

# O aluno pode criar outras funcoes que ache necessario

def checkvalido(resposta, i, j):
	lista1 = []  # lista1, 2 e 3: listas para verificar existencia de dois numeros iguais em linhas, colunas e quadrados, respectivamente
	for z in resposta[i]:  # verifica a existencia de numeros iguais na linha do ultimo numero adicionado
		if z == 0:
			continue
		if z in lista1:  # se existe algum, retorna False
			return False
		lista1.append(z)
	lista2 = []
	for z in resposta:  # verifica a existencia de numeros iguais na coluna do ultimo numero adicionado
		if z[j] == 0:
			continue
		if z[j] in lista2:  # se existe algum, retorna False
			return False
		lista2.append(z[j])
	lista3 = []


	square = (int(j/3)+1) * (int(i/3)+1)  # descobre numero do quadrado onde foi adicionado o ultimo numero
	if square % 3 == 1:  # caso seja o quadrado 1, 4 ou 7
		for j in range(3):  # executa o codigo para as tres colunas do quadrado
			for i in range((square-1), (square+2)):  # tenta encontrar numeros iguais dentro dos quadrados, caso encontre retorna False, caso contrario retorna True
				if resposta[i][j] in lista3 :
					return False
				if resposta[i][j] == 0:
					continue
				lista3.append(resposta[i][j])
		return True
	if square % 3 == 2:  # caso seja o quadrado 2, 5 ou 8
		for j in range(3, 6):
			for i in range((square-2), (square+1)):
				if resposta[i][j] in lista3 :
					return False
				if resposta[i][j] == 0:
					continue
				lista3.append(resposta[i][j])
		return True
	for j in range(6, 9):  # caso seja o quadrado 3, 6 ou 9
		for i in range((square-3), (square)):
			if resposta[i][j] in lista3 :
				return False
			if resposta[i][j] == 0:
				continue
			lista3.append(resposta[i][j])
	return True


def recursive(resposta, i, j):
	if resposta[i][j] == 0:
		while True:
			if resposta[i][j] == 9:
				resposta[i][j] = 0
				return False
			resposta[i][j] += 1
			resp = 0
			if checkvalido(resposta, i, j):
				if j == 8:
					if i == 8:
						return True
					resp = recursive(resposta, i+1, 0)
				else:
					resp = recursive(resposta, i,j+1)
				if resp:
					return True




				'''		return True
					return recursive(resposta,i+1,0)
				return recursive(resposta,i,j+1)

				if i == 8:
					if j == 8:
						return True
					if recursive(resposta, 0, j+1):
						return True
				else:
					if recursive(resposta, i+1, j):
						return True'''


	else:
		if j == 8:
			if i == 8:
				return True
			j = 0
			i += 1
		else:
			j += 1
		if recursive(resposta, i, j):
			return True


# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario
def resolve(resposta):
    # Implementar a funcao e trocar o valor de retorno
	return recursive(resposta, 0, 0)
