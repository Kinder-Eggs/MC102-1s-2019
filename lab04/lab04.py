#Gabriel Costa Kinder - 234720
c1=int(input())
c2=int(input())
c3=int(input())
c4=int(input())
if ((c1+c2)==(c3+c4)):
    print("sim")
elif((c1+c3)==(c2+c4)):
    print("sim")
elif((c1+c4)==(c2+c3)):
    print("sim")
elif(c1==(c2+c3+c4)):
    print("sim")
elif(c2==(c1+c3+c4)):
    print("sim")
elif(c3==(c1+c2+c4)):
    print("sim")
elif(c4==(c1+c2+c3)):
    print("sim")
else:
    print("nao")
