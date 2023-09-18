def snint(list):
    for i in range(0,101):
        if i not in list:
            return i


ans = []
for i in range(int(input(""))):
    ship = []
    a,b=[],[]
    len = int(input(""))
    ship = input().strip().split(" ")
    i=0
    dyn = ship.copy()
    while True:
        if str(i) not in ship:
            for i in dyn:a.append(int(i))
            break

        elif dyn.count(str(i))==1:
            a.append(int(i))
            dyn.remove(str(i))

        elif dyn.count(str(i))>=2:
            a.append(int(i))
            dyn.remove(str(i))

            while str(i) in dyn:
                b.append(int(i))
                dyn.remove(str(i))

        else:
            pass

        i+=1
                
    ans.append(snint(a)+snint(b))

    
for i in ans:print(i)
