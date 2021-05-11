def imprime(s1):
    s2=s1.split(" ")
    s2=sorted(s2,key=len,reverse=True)
    for temp in s2:
        print(temp, end=" ")
    print("")

N=int(input(""))
lista=[]
for i in range(0,N):
    temp=input("")
    lista.append(temp)

for i in lista:
    imprime(i)
print("")
