def mdc(n1,n2):
    resto = None
    while (resto!=0):
        resto = n1 % n2
        n1  = n2
        n2  = resto
    return n1 

n=int(input())
for i in range(n):
    s1=input()
    tmp=s1.split(" ")
    if(tmp[3]=="+"):
        dividendo=str((int(tmp[0])*int(tmp[6]))+(int(tmp[4])*int(tmp[2])))
        divisor=str(int(tmp[2])*int(tmp[6]))
    elif(tmp[3]=="-"):
        dividendo=str((int(tmp[0])*int(tmp[6]))-(int(tmp[4])*int(tmp[2])))
        divisor=str(int(tmp[2])*int(tmp[6]))
    elif(tmp[3]=="*"):
        dividendo=str(int(tmp[0])*int(tmp[4]))
        divisor=str(int(tmp[2])*int(tmp[6]))
    else:
        dividendo=str(int(tmp[0])*int(tmp[6]))
        divisor=str(int(tmp[4])*int(tmp[2]))
    maior_divisor=mdc(int(dividendo),int(divisor))
    dividendo_dois=str(int(dividendo)//maior_divisor)
    divisor_dois=str(int(divisor)//maior_divisor)
    print('%s/%s = %s/%s' %(dividendo,divisor,dividendo_dois,divisor_dois))