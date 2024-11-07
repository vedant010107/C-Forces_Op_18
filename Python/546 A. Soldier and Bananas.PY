n=list(map(int,input().split()))
rupp=0
for i in range(1,n[2]+1):
    rupp+=i*n[0]
if rupp>n[1]:
    bor=rupp-n[1]
else:
    bor=0
print(bor)