ans=[]
def countMax(list):
    a = 0
    c = 0
    for i in set(list):
        if list.count(i)==len(list)-1:
            c=list.count(i)
            a=i
    return a


for i in range(int(input())):
    perm = []
    fin = []
    a = []
    n=int(input())
    for i in range(n):
        perm.append(input().strip().split())

    for i in range(len(perm)):
        a.append(perm[i][0])
    fin.append(countMax(a))

    a = []

    for i in range(len(perm)):
        a.append(perm[i][-1])
    fin.append(countMax(a))

    a=[]
    ele=fin[0]
    while len(fin)<len(perm):
        for i in perm:        
            if ele in i: 
                a.append(i[i.index(ele)+1])        
        fin.insert(fin.index(ele)+1,countMax(a))       
        a = []
        ele = fin[fin.index(ele)+1]
    ans.append(fin)
    if n==3:
        ans.remove(fin)
        fin.pop(1)
        for i in perm:
            for j in i:
                if j not in fin:
                    fin.insert(1,j)
                    ans.append(fin)
                    break
for i in ans:
    for j in i:
        print(j,end=" ")
    print()
