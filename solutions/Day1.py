N=int(input())
for i in range(N):
    temp=input()
    s2=temp.split(" ")
    s2=sorted(s2,key=len,reverse=True)
    nova=""
    for j in s2:
        nova+=j+" "
    print(nova[:-1])