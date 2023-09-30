def sum_(n):
    n -= 1
    n3 = n // 3
    n5 = n // 5
    n15 = n // 15
    s3 = (n3 * (n3 + 1)) // 2
    s5 = (n5 * (n5 + 1)) // 2
    s15 = (n15 * (n15 + 1)) // 2
    tot = 3 * s3 + 5 * s5 - 15 * s15
    return tot

ans = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans.append(sum_(n))

for i in ans:
    print(i)

