m1=[[1,2,3],
    [1,2,1],
    [2,3,1]]
m2=[[0,0,0],
    [0,0,0],
    [0,0,0]]
c=int(input("enter the scalar value:"))
for i in range(len(m1)):
    for j in range(len(m1[0])):
        m2[i][j]=m1[i][j]*c

for r in m2:
   print(r)