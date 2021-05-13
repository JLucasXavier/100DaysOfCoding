def imprimir(tmp):
    station=[]
    b=[]
    teste=tmp.split(" ")
    maximo = max(teste, key=int)
    minimo=min(teste,key=int)
    n=int(maximo)
    for item in range(len(teste)-1,-1,-1):
        if(int(teste[item])==n):
            b.insert(0,teste[item])
            n=n-1
            if(len(station)>0):
                while(((str(n)) in station)==True):
                    b.insert(0,station[0])
                    station.pop(0)
                    n=n-1
        else:
            station.insert(0,teste[item])
    for item in range(len(station)):
        b.insert(0,station[item])
        temp=sorted(b)
        if(b!=temp):
            return "No"
    return "Yes"
n=4
while(n!=0):
    tmp=""
    n=int(input())
    if(n==0):
        break
    while(tmp!="0"):
        tmp=input()
        if(tmp=="0"):
            print()
            break
        else:
            print(imprimir(tmp))