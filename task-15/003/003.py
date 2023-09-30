t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    while n % 2 == 0:
        n //= 2
    f= 3

   
    while f**2 <= n:
        if n % f == 0:
            n //= f
        else:
            f += 2 
    print(n)
