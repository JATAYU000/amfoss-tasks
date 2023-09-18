n=int(input())
l=list(map(int,input().split()))
min = min(l)
if l.count(min)>=2:
    print("Still Aetheria")
else:
    print(l.index(min)+1)
