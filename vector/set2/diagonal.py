import numpy as np
n = int(input("Enter the order of matrix :"))
print("Enter the elements of matrix :")
matrix=[]
for i in range (n):
    for j in range (n):
        ele = int(input())
        matrix.append(ele)
matrix = np.array(matrix)
matrix = matrix.reshape(n,n)
print("the matrix is")
print (matrix)
diagonal_matrix=[]
print("The diagonal matrix is")
for i in range (n) :
    for j in range (n) :
        if i==j:
            diagonal_matrix.append(matrix[i][j])
        else:
            diagonal_matrix.append(0)
diagonal_matrix = np.array(diagonal_matrix)
diagonal_matrix= diagonal_matrix.reshape(n,n)
print(diagonal_matrix)