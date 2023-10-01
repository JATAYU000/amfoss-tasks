ans=[]
for i in range(int(input())):
    sort=[]
    val='1'
    n = int(input())
    l = list(map(int,input().split()))
    sort.append(l.pop(0))
    l2 = l.copy()
   
   
    for i in l:
        if i>=sort[-1]:
            sort.append(l2.pop(0))
            val+='1'
        else:
            l=l2.copy()
            if i<=sort[0]:
                sort.append(l2.pop(0))
                val+='1'
            l=l2.copy()
            for i in l:
                if i>=sort[-1] and i<=sort[0]:
                    sort.append(l2.pop(0))
                    val+='1'
                else:
                    l2.pop(0)
                    val+='0'
                
            break
    
    print(val)  
