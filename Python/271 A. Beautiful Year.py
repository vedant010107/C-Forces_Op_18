def diy(n):
    n+=1
    l=[]
    n=str(n)
    c=0
    for i in n:
        if i in l:
            c=1     
        else:
            l.append(i)
    if (c==0):
        return int(n)
    else:
        return diy(int(n))
n=int(input())
print(diy(n))
