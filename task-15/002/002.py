ans=[]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fib=[1,2]
    s=2
    while fib[-1]<n:
        a=fib[-1]+fib[-2]
        if a>n:
            break
        if a%2==0:
            s+=a
        fib.append(a)
    ans.append(s)
for i in ans:print(i)
