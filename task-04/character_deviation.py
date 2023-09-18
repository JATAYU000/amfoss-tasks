l=[]
for i in range(int(input())):
    h=input()
    ans=6
    g='amfoss'
    for j in range(6):
        if g[j]==h[j]:
            ans-=1
    l.append(ans)

for i in l:print(i)    
