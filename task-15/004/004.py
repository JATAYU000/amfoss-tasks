def generate_pls():
    x = range(100, 1000)
    pls=[]
    for i in x:
        for j in x:
            P = i * j
            if str(P) == str(P)[::-1]:
                 pls.append(P)
    pls.sort(reverse=True)
    """
    first get all combinations prod ,check palindrome,
    reverse the list for next functions smooth working
    next function checks num thats less than n since this pls has bigger ans too
    thats y reversed
    """
    return pls

def find_LP(n, pls):
    for P in pls:
        if P < n:
            return P


    
t = int(input().strip())
pls = generate_pls()
    
for _ in range(t):
    n = int(input().strip())#101110
    LP = find_LP(n, pls)
    print(LP)
    
