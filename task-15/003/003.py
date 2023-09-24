t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    while n % 2 == 0:
        n //= 2
    f= 3

    """first getting the odd number 
    then trying with odd factors < root n"""
    while f**2 <= n:
        if n % f == 0:
            n //= f
        else:
            f += 2 
    r = n
    print(r)
