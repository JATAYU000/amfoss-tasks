import math
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    lcm = 1
    for i in range(2, n + 1):
        gcd = math.gcd(lcm, i)
        lcm = (lcm * i) // gcd
    print(lcm)
