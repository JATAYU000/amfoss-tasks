def generator():
    x = range(100, 1000)
    pls=[]
    for i in x:
        for j in x:
            P = i * j
            if str(P) == str(P)[::-1]:
                 pls.append(P)
    pls.sort(reverse=True)
    return pls


def find_LP(n, pls):
    for P in pls:
        if P < n:
            return P


    
t = int(input().strip())
pls = generator()
for _ in range(t):
    n = int(input().strip())
    LP = find_LP(n, pls)
    print(LP)
    
