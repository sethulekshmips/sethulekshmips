m1=[[1,2,3],
    [2,3,4],
    [4,5,6]]
m2=[[2,3,4],
    [4,2,3],
    [4,5,2]]
m3=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        m3[i][j]=m1[i][j]*m2[i][j]

print("hardmardproduct of matrix:",m3)