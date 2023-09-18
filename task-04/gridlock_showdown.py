l_ans=[]
for i in range(int(input(""))):
    l=[]
    ans = True
    for i in range(3):
        l.append(list(input()))
    for i in range(3):

        #diagonal first

        if l[0][0]==l[1][1]==l[2][2]:
            l_ans.append(l[1][1])
            ans = True
            break

        #diagonal second

        elif l[0][2]==l[1][1]==l[2][0]:
            l_ans.append(l[1][1])
            ans = True
            break
        
        #vertical

        elif l[i][0]==l[i][1]==l[i][2]:
            l_ans.append(l[i][1])
            ans = True
            break

        #Horizontal

        elif l[0][i]==l[1][i]==l[2][i]:
            l_ans.append(l[0][i])
            ans = True
            break

        #DRAW

        else:
            ans = False
    if not ans:
        l_ans.append("DRAW")
for i in l_ans:
    print(i) if i !='.' else print('DRAW')
