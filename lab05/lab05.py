#Gabriel Kinder - 234720
t=int(input())
c=int(input())
fluxo = input()
lfluxo = fluxo.split() #transforma em lista
lfluxo = list(map(int, lfluxo)) #transforma em int
i=0
total = 0 #variavel para a soma continua
ver = 1 #variavel para verificacao
for i in range(t):
    total = total + lfluxo[i] #soma total
    if(total>=c): #verificacao de conclusao
        print("sim")
        print(i+1) #tempo concluido
        ver = 0 #nao executar print da destruicao da nave
        break
if(ver): #destruicao da nave
    print("nao")
    print(t+1) #tempo de destruicao da nave
