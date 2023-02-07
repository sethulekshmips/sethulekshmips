X=[[1,2,3],
    [3,4,5],
    [4,5,6]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
#for i in range(len(m1[0])):
 #   for j in range(len(m1)):
  #      result = m1[j][i]
result = [[X[j][i] for j in range (len (X))] for i in range (len (X[0]))]

for r in result:
    print(r)
