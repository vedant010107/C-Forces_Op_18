n=list(map(int,input().split()))
for i in range(1,n[1]+1):
    if n[0]%10==0:
        n[0]/=10
    else:
        n[0]-=1
print(int(n[0]))