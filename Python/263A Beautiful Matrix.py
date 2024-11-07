matrix=[]
for i in range(5):
    a=list(map(int,input().split()))
    matrix.append(a)
count=0

while(matrix[2]!=[0,0,1,0,0]):
    if matrix[2][i]!=0:
        if i>2:
            matrix[2][i]=0
            matrix[2][i-1]=1
            count+=1
            
        elif i<2:
            matrix[2][i]=0
            matrix[2][i+1]=1
            count+=1
        else:
            count+=0
while(matrix[2][2]!=1):
    if matrix[i][2]!=0:
        if i>2:
            matrix[i][2]=0
            matrix[i-1][2]=1
            count+=1
        elif i<2:
            matrix[i][2]=0
            matrix[i+1][2]=1
            count+=1
        else:
            count+=0
print(count)