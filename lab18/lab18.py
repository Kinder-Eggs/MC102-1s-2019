# Gabriel Costa Kinder - 234720
import sys

def main():
	matriz, div = get_matrix()  # chama a funcao get_matrix para obter a matriz de convolucao e o divisor
	img, size = get_img()  # chama a funcao get_img para obter uma matriz com os valores dos pixels da img e seu tamanho
	new_img = gen_new_img(div, matriz, img)  #  faz a convolucao utilizando matriz e div na img
	print("P2")  # sequencia de prints padrao
	print(size[0] + " " + size[1])
	print("255")
	for i in range(len(new_img)):
		for j in new_img[i]:
			print(str(j), end=" ")  # printa cada um dos pixels da imagem nova com os espacos estabelecidos
		print(" ")

def get_matrix():
	matriz = []  # cria uma matriz vazia
	matriztxt = open(sys.argv[2], "r")  # abre o arquivo especificado que deve conter a matriz
	div = matriztxt.read(1)  # le o primeiro caracter para obter o valor do divisor
	matriztxt.read(1)  # pula um caracter
	for i in range(3):  # repete tres vezes a operacao para ler a linha da matriz
		linha = []  # matriz onde sera colocado os valores de cada linha
		aux2 = 0  # variaveis para auxiliar no algoritmo
		counter = 0
		while True:  # repete ate atingir um break
			aux = matriztxt.read(1)  # salva o proximo valor em aux
			if counter == 3:  # caso counter atinja tres (leu os tres valores existentes em cada linha) da break
				break
			if aux == " ":  # caso encontre um espaco vazio passa para o proximo valor
				continue
			if aux == "-":  # salva aux2 como -1 para saber que o valor eh negativo e passa para ler o proximo valor
				aux2 = -1
				continue
			if aux2==0:  # caso aux2 seja zero salva o valor encontrado como positivo na matriz linha e aumenta counter em 1
				linha.append(int(aux))
				counter += 1
			else:  # caso aux2 nao seja zero (ou seja, -1) salva o valor como negativo, zera aux2 e aumenta o counter em 1
				linha.append(int(aux)*-1)
				aux2=0
				counter += 1
		matriz.append(linha)  # salva a linha na matriz e continua para ler a proxima linha
	matriztxt.close()  # fecha o arquivo aberto
	return matriz, div  # retorna os valores da matriz e o divisor


def get_img():
	imgmx = []  # cria uma matriz vazia onde ficara a imagem
	img = open(sys.argv[1], "r")  # abre o arquivo onde localiza-se a imagem
	img.read(3)  # pula os tres primeiros caracteres("'P''2''\n'")
	size = get_until_newl(img).split()  # utiliza a funcao get_until_newl para obter a linha completa, e salva as dimensoes da imagem em size como uma lista
	maxpx = get_until_newl(img)  # magnitude maxima de cada pixel (sempre 255)
	aux = img.read().split()  # le todo o restante do arquivo completo e salva todos os valores como aux em formato de lista
	for i in range(int(size[1])):  # algoritmo para obter uma lista onde cada lista dentro dela refere-se a uma linha da imagem
		aux2 = []
		for j in range(int(size[0])):
			aux2.append(aux[j+(i*int(size[0]))])
		imgmx.append(aux2)
	img.close()  # fecha o arquivo da imagem
	return imgmx, size  # retorna a lista com os valores da imagem e seu tamanho


def get_until_newl(file):
	string = ""
	while True:  # le caractere por caractere e concatena cada um em string ate atingir um `\n` (proxima linha)
		aux = file.read(1)
		if aux == "\n":
			break
		string += aux
	return string  # retorna a string


def gen_new_img(div, matriz, img):
	new_img = [[0 for i in range(len(img[j]))] for j in range(len(img))]  # gera uma lista identica a imagem original porem com todos os valores iguais a zero
	img = [[int(i) for i in img[j]]for j in range(len(img))]  # transforma todos os valores da imagem em ints (estavam como strings)
	for i in range(len(img)):  # loop para leitura de cada valor contido na imagem para iniciar o processo de convolucao
		for j in range(len(img[i])):
			if i == 0 or j == 0:  # caso esteja na borda de cima ou da esquerda mantem os pixels da imagem convolutada e original iguais
				new_img[i][j] = img[i][j]
			else:
				try:  # tenta fazer o calculo para o valor do novo pixel [i][j] da nova imagem utilizando matriz e div
					new_img[i][j] = (matriz[0][0]*img[i-1][j-1] + matriz[0][1]*img[i-1][j] + matriz[0][2]*img[i-1][j+1] + matriz[1][0]*img[i][j-1] + matriz[1][1]*img[i][j] + matriz[1][2]*img[i][j+1] + matriz[2][0]*img[i+1][j-1] + matriz[2][1]*img[i+1][j] + matriz[2][2]*img[i+1][j+1]) / int(div)
					if new_img[i][j] < 0:  # caso valor seja menor que zero iguala a zero
						new_img[i][j] = 0
					elif new_img[i][j] > 255:  # caso valor seja maior que 255 iguala a 255
						new_img[i][j] = 255
					else:  # caso esteja no intervalo transforma em int (era float)
						new_img[i][j] = int(new_img[i][j])
				except:  # excessao quando esta na borda da direita ou inferior (index out of range), quando ocorre mantem pixels iguais
					new_img[i][j] = img[i][j]
	return new_img  # retorna imagem convolutada

main()