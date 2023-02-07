def lowermat(matrix,row,col):
    for i in range(0,row):
        for j in range (0,col):
            if(i<j):
                print("0",end=" ")
            else:
                print(matrix[i][j],end=" ")
        print(" ")

def uppermat(matrix, row, col):

    for i in range(0, row):

        for j in range(0, col):

            if (i > j):
                print("0", end=" ");

            else:
                print(matrix[i][j],
                  end=" ");

        print(" ");


matrix=[[1,2,3],
        [2,3,4],
        [2,1,2]]
row=3
col=3
print("lowertriangle matrix:")
lowermat(matrix,row,col)
print("upper traingularmatrix:")
uppermat(matrix,row,col)