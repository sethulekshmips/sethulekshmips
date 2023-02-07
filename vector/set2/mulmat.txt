
x=[[1,2,3],
   [2,1,3],
   [4,2,3]]
y=[[1,2,3],
   [4,3,1],
   [2,4,2]]
m=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
       for k in range(len(y)):
          m[i][j]+=x[i][k]*y[k][j]

for r in m:
      print(r)