t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    lcm = 1
    for i in range(2, n + 1):
        gcd = math.gcd(lcm, i)
        lcm = (lcm * i) // gcd
        # its easy to just divide product with greatest common divisor 
        # run the in a loop to find lcm of the prev lcm and new num again nd again
    ans = lcm
    print(ans)
