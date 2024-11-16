n=list(map(int,input().split()))
h=list(map(int,input().split()))
w=0
for i in h:
    if i>n[1]:
        w+=2
    else:
        w+=1
print(w)