t=int(input())
for i in range(t):
    n=int(input())
    dn=list(map(int,input().split()))
    if len(dn)==2*n:
        if n==1:
            count=0
            for i in dn:
                if i==1:
                    count+=1
            if count%2==0:
                print(0,0)
            else:
                print(1,1)
        else:
            count=0
            for i in dn:
                if i==1:    
                    count+=1
            if count%2==0:
                mina=0
            else:
                mina=1
            if count>n and count!=(2*n):
                if count%2==0:
                    maxa=count-((n+1)//2)
                else:
                    maxa=count-n
            elif count==(2*n):
                maxa=0
            else:
                maxa=count
            print(mina,maxa)