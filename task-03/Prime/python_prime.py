list=[2]
x=int(input("Enter the number limit: "))+1
if x == 1:
    print("No prime")
elif x == 2:
    print(2)
else:
    for i in range(2,x):
        c=len(list)
        a=0
        for j in list:
            if i%j==0:
                pass
            else:a+=1
        if a==c:
            list.append(i)

    for i in list:print(i)