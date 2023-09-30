for i in range (int(input())):
    n=input()
    l=list(map(int,input().split()))
    prev=l[-1]
    two=0
    if len(l)!=1:
        for i in l[-2::-1]:
            while i>=prev:
                i//=2
                two+=1
                if i==0 and prev==0:
                    two=-1
                    break
            prev=i
        print(two)
    else:
        print(0)
