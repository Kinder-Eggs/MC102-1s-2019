# Gabriel Kinder - 234720

wonrnd = 0  # Variavel de verificacao


def MultiplierCheck (hit):  # Funcao para verificar multiplicadores
    i = 1
    soma = 0
    while True:  # verificacao de numero perfeito
        if hit % i == 0:
            soma += i
        if soma == hit:
            return hit*3
        if i > hit:
            break
        i += 1
    i = 1
    soma = 0
    while True:  # verificacao de numero triangular
        soma += i
        if soma == hit:
            return hit*2
        if i > hit/2:
            return hit
        i += 1


def CheckHit (hit):  # Funcao para checar inimigo atingido
    if hit > 0:
        return 1
    if hit < 0:
        return -1


def DanoRyu (hit, pvken):  # Funcao para causar dano no Ken
        print("Ken:", pvken, "-", hit, "=", pvken - hit)
        pvken -= hit
        return pvken


def DanoKen (hit, pvryu):  # Funcao para causar dano no Ryu
        print("Ryu:", pvryu, "-", hit, "=", pvryu - hit)
        pvryu -= hit
        return pvryu


def Round(wonrnd):  # Funcao que roda o jogo
    pvryu = 2000  # PVs iniciais
    pvken = 2000
    hit = int(input())  # Verificacao do hit
    perhit = CheckHit(hit)  # Verificacao de quem ataca: +1 ataque do Ryu, -1 ataque do Ken
    if perhit == -1:  # Manter valores de hit positivos
        hit *= -1
    hit = MultiplierCheck(hit)  # Chama a funcao que verifica os multiplicadores
    while True:  # loop primeiro round
        nexthit = int(input())  # Verificacao do proximo hit
        pernhit = CheckHit(nexthit)  # Verificacao de quem ataca no proximo hit
        if pernhit == -1:
            nexthit *= -1
        nexthit = MultiplierCheck(nexthit)  # Multiplicador do proximo hit
        if perhit == 1 and hit >= pvken or perhit == -1 and hit >= pvryu:  # Verificacao se o dano e suficiente
            if perhit == 1:
                pvken = DanoRyu(hit, pvken)
            if perhit == -1:
                pvryu = DanoKen(hit, pvryu)
            if perhit == 1:
                wonrnd += 1
                hit = nexthit
                perhit = pernhit
                break
            if perhit == -1:
                wonrnd -= 1
                hit = nexthit
                perhit = pernhit
                break
        if perhit == pernhit:  # Soma os dois danos se o alvo for o mesmo
            hit += nexthit
        else:  # Se nao for, causa o dano
            if perhit == 1:
                pvken = DanoRyu(hit, pvken)
                hit = nexthit
                perhit = pernhit
            elif perhit == -1:
                pvryu = DanoKen(hit, pvryu)
                hit = nexthit
                perhit = pernhit
        if perhit == 1 and hit >= pvken or perhit == -1 and hit >= pvryu:  # Verifica se proximo dano e suficiente
            if perhit == 1:
                pvken = DanoRyu(hit, pvken)
            if perhit == -1:
                pvryu = DanoKen(hit, pvryu)
            if perhit == 1:
                wonrnd += 1
                hit = 0
                perhit = pernhit
                break
            if perhit == -1:
                wonrnd -= 1
                hit = 0
                perhit = pernhit
                break
    pvken = 2000  # Reseta PVs
    pvryu = 2000
    while True:  # Loop segundo round
        nexthit = int(input())
        pernhit = CheckHit(nexthit)
        if pernhit == -1:
            nexthit *= -1
        nexthit = MultiplierCheck(nexthit)
        if perhit == 1 and hit >= pvken or perhit == -1 and hit >= pvryu:
            if perhit == 1:
                pvken = DanoRyu(hit, pvken)
            if perhit == -1:
                pvryu = DanoKen(hit, pvryu)
            if perhit == 1:
                wonrnd += 1
                hit = nexthit
                perhit = pernhit
                break
            if perhit == -1:
                wonrnd -= 1
                hit = nexthit
                perhit = pernhit
                break
        if perhit == pernhit:
            hit += nexthit
        elif hit == 0:
            hit += nexthit
            perhit = pernhit
        else:
            if perhit == 1:
                pvken = DanoRyu(hit, pvken)
                hit = nexthit
                perhit = pernhit
            elif perhit == -1:
                pvryu = DanoKen(hit, pvryu)
                hit = nexthit
                perhit = pernhit
        if perhit == 1 and hit >= pvken or perhit == -1 and hit >= pvryu:
            if perhit == 1:
                pvken = DanoRyu(hit, pvken)
            if perhit == -1:
                pvryu = DanoKen(hit, pvryu)
            if perhit == 1:
                wonrnd += 1
                break
            if perhit == -1:
                wonrnd -= 1
                break
        if pernhit == 1 and nexthit >= pvken or perhit == -1 and nexthit >= pvryu:
            if pernhit == 1:
                pvken = DanoRyu(nexthit, pvken)
                wonrnd += 1
                break
            if pernhit == -1:
                pvryu = DanoKen(nexthit, pvryu)
                wonrnd -= 1
                break
    if wonrnd == 2:
        print("Ryu venceu")
    elif wonrnd == -2:
        print("Ken venceu")
    else:
        print("empatou")


Round(wonrnd)
