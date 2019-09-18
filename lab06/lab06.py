#Gabriel Kinder - 234720
cap=int(input()) #ler Capacidade
aux=int(input()) #variavel auxiliar
while aux!=0:
    if (aux>0): #se carro entrando
        if (aux>cap): #se carro muito grande
            print ("Veiculo muito grande! Capacidade restante:", cap)
        else: #se carro pode entrar
            cap=cap-aux
            print ("Seja bem-vindo! Capacidade restante:", cap)
    if (aux<0): #se carro saindo
        cap=cap-aux
        print("Volte sempre! Capacidade restante:", cap)
    aux=int(input())
