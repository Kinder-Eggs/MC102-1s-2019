# Gabriel Kinder - 234720
pvryu = 50  # pontos de vida iniciais Ryu
pvken = 50  # pontos de vida iniciais Ken
round = 0  # Variavel verificadora de round
aux=int(input())  # variavel para contabilizar o primeiro dano
while (True):  # loop primeiro round
    aux2 = int(input())  # variavel para contabilizar proximo dano
    if (aux < 0 and aux2 < 0 or aux > 0 and aux2 > 0):  # se ambos os danos forem do mesmo personagem
        aux += aux2  # somam-se os danos
        if(aux*-1 >= pvryu):  # se proximo hit de Ken maior que os pontos de vida de Ryu, printa o hit e passa o round
            print("Ryu:", pvryu, "-", aux * -1, "=", pvryu + aux)
            round += 1  # variavel que contabiliza rounds vencidos
            break
        elif (aux >= pvken):  # se proximo hit de Ryu maior que os pontos de vida de Ken, printa o hit e passa o round
            print("Ken:", pvken, "-", aux, "=", pvken - aux)
            round -= 1
            break
    else:
        if (aux < 0):  # Se < 0 ataque do Ken (Ryu perde pv)
            print("Ryu:", pvryu, "-", aux * -1, "=", pvryu + aux)
            pvryu += aux  # novo pv
        elif (aux > 0):  # Se > 0 ataque do Ryu (Ken perde pv)
            print("Ken:", pvken, "-", aux, "=", pvken - aux)
            pvken -= aux  # novo pv
        aux = aux2
        if(aux*-1 >= pvryu):  # caso prox dano de Ken seja > pvryu, finaliza o round
            print("Ryu:", pvryu, "-", aux * -1, "=", pvryu + aux)
            round += 1
            break
        elif(aux >= pvken):  # caso prox dano de Ryu seja > pvken, finaliza o round
            print("Ken:", pvken, "-", aux, "=", pvken - aux)
            round -= 1
            break

pvryu = 50  # Reset dos pvs para novo round
pvken = 50
aux = 0

while (True): # loop segundo round
    aux2 = int(input())
    if (aux < 0 and aux2 < 0 or aux > 0 and aux2 > 0):
        aux += aux2
        if(aux*-1 >= pvryu):
            print("Ryu:", pvryu, "-", aux * -1, "=", pvryu + aux)
            round += 1
            break
        elif (aux >= pvken):
            print("Ken:", pvken, "-", aux, "=", pvken - aux)
            round -= 1
            break
    else:
        if (aux < 0):
            print("Ryu:", pvryu, "-", aux * -1, "=", pvryu + aux)
            pvryu += aux
        elif (aux > 0):
            print("Ken:", pvken, "-", aux, "=", pvken - aux)
            pvken -= aux
        aux = aux2
        if (aux*-1 >= pvryu):
            print("Ryu:", pvryu, "-", aux * -1, "=", pvryu + aux)
            round += 1
            break
        elif (aux >= pvken):
            print("Ken:", pvken, "-", aux, "=", pvken - aux)
            round -= 1
            break

if(round==0):  # Se Ken ganhou um e Ryu outro
    print("empatou")
elif(round==2):  # Se Ken ganhou ambos
    print("Ken venceu")
elif(round==-2):  # Se Ryu ganhou ambos
    print("Ryu venceu")
