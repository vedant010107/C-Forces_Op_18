s=input()
count_upper=0
count_lower=0
for i in s:
    if i>='a':
        count_lower+=1
        
    else:
        count_upper+=1.
        
if count_lower>=count_upper:
    print(s.lower()) 
else:
    print(s.upper()) 

