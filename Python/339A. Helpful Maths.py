n=list(map(int,input().split("+")))
n.sort()
for i in range(len(n)):
    print(f"{n[i]}",end="")
    if i!=len(n)-1:
        print("+",end="")
    
    
    
    