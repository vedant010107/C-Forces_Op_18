n=int(input())
count=0
for i in range(5,1,-1):
    count+=n//i
    n=n%i
print(count)