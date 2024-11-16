n=int(input())
maxim=[]
maxi=0
for i in range(n):
    stop=list(map(int,input().split()))
    maxi+=stop[1]-stop[0]
    maxim.append(maxi)
a=max(maxim)
print(a)