# Gabriel Costa Kinder - 234720

def main():
    texto = input().lower().split()  # recebe o texto, coloca tudo em letra minuscula e entao divide em lista
    while True:  
        result = vercoord(texto)  # chama funcao que retorna os valores secretos da mensagem
        if result[0] != 0 and result[1] != 0:  # se foi devolvido resultados diferentes de zero imprime eles
            print(result[0], '-', result[1])
        if len(texto) == 0:  # caso a lista texto tenha sido completamente lida, encerra o programa
            break
        del texto[0]  # apaga o valor de texto que foi lido
        if len(texto) == 0:  # caso tenham acabado os valores de texto encerra o programa
            break


def vercoord (texto):
    result = [0,0]  # atribui lista com duas variaveis para o resultado
    
# verifica se a palavra no indice 0 seria um dos codigos e entao atribui o valor respectivo ao indice 0 do resultado e chama outra funcao para descobrir o angulo

    if texto[0] == "mercurio":
        result[0] = 'N'
        result[1] = vergrau(texto)
        
    elif texto[0] == "venus":
        result[0] = 'NE'
        result[1] = vergrau(texto)

    elif texto[0] == "terra":
        result[0] = 'L'
        result[1] = vergrau(texto)

    elif texto[0] == "marte":
        result[0] = 'SE'
        result[1] = vergrau(texto)

    elif texto[0] == "jupiter":
        result[0] = 'S'
        result[1] = vergrau(texto)

    elif texto[0] == "saturno":
        result[0] = 'SO'
        result[1] = vergrau(texto)

    elif texto[0] == "urano":
        result[0] = 'O'
        result[1] = vergrau(texto)

    elif texto[0] == "netuno":
        result[0] = 'NO'
        result[1] = vergrau(texto)

    return result  # retorna resultado obtido


def vergrau(texto): 
    while True:  # loop ate encontrar o angulo
        
# procura a palavra no indice 0 que representa o angulo e a retorna

        if texto[0] == "verde":  
            return 30

        elif texto[0] == "amarelo":
            return 45

        elif texto[0] == "vermelho":
            return 60
    
        else:
            del texto[0]  # caso nao encontre nenhuma palavra no indice 0, apaga a palavra e tenta novamente

main()
