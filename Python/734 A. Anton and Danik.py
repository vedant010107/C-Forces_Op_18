n=int(input())
s=input()
if len(s)==n:
    countA=s.count('A')
    countD=s.count('D')
    if countA>countD:
        print("Anton")
    elif countA==countD:
        print("Friendship")
    else:
        print("Danik")

    


