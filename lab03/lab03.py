#Gabriel Costa Kinder - 234720
d=float(input())
r=d/2
h=float(input())
a=float(input())
b=float(input())
c=float(input())
vc=3.14*(r**2)*h*1000
if(vc>a):
    print ("posto A foi reabastecido")
    vc=vc-a
else:
    print ("posto A nao foi reabastecido")
if(vc>b):
    print ("posto B foi reabastecido")
    vc=vc-b
else:
    print ("posto B nao foi reabastecido")
if(vc>c):
    print ("posto C foi reabastecido")
else:
    print ("posto C nao foi reabastecido")
