vect = []
for i in range(int(input(""))):
    vect.append(input().strip().split(" "))

sum_x, sum_y, sum_z = 0, 0, 0

for i in range(len(vect)):
    sum_x+=int(vect[i][0])
    sum_y+=int(vect[i][1])
    sum_z+=int(vect[i][2])

if sum_x==0 and sum_y==0 and sum_z==0:print("YES")
else:print("NO")
