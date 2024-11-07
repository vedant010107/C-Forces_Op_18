n=list(map(int,input().split()))
count=0
while (n[0]<=n[1]):
    n[0]*=3
    n[1]*=2
    count+=1
print(count)