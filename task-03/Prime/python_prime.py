list=[2]
for i in range(2,int(input("Enter the number limit: "))+1):
    
    c=len(list)
    a=0
    
    for j in list:
        if i%j==0:
            pass
        else:a+=1
    if a==c:
        list.append(i)

for i in list:print(i)
    
