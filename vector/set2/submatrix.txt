x=[[2,4,6],
   [3,5,7],
   [9,8,10]]
y=[[1,2,3],
   [4,3,2],
   [6,5,8]]
z=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(y)):
    for j in range(len(y[0])):
        z[i][j] = y[i][j]-x[i][j]

for r in z:
    print(r)