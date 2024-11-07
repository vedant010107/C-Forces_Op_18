n=int(input())
s=[]
for i in range(n):
    s.append(input())
    count=0
    for i in range(len(s)):
        if s[i]==s[i+1]:
            s.pop(i+1)
            i=0
            count+=1
            
    print(count)
