def quality(l, r):
    l=str(l).zfill(len(str(r)))
    return sum(abs(int(l[i])-int(str(r)[i])) for i in range(len(l)))


def maxQuality(l, r):
    mq = 0
    
    for i in range(l, r + 1):
        for j in range(i+1, r + 1):
            q = quality(i, j)
            mq = max(mq, q)
    
    return mq
ans=[]
for i in  range(int(input())):
    l, r = map(int,input().strip().split())
    ans.append(maxQuality(l,r))
for i in ans:print(i)
