word=input()
dict={}
for i in word:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

if len(dict)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
        