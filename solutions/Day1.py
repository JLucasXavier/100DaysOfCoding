N=int(input())
for i in range(N):
    temp=input()
    s2=temp.split(" ")
    s2=sorted(s2,key=len,reverse=True)
    nova=""
    for j in range(len(s2)):
        if(j==len(s2)-1):
            nova=nova+s2[j]
        else:
            nova=nova+s2[j]+" "
    print(nova)