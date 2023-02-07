import numpy as np
n= int(input("enter the oreder of matrix"))
print("enter the elements in matrix:")
matrix=[]
for i in range(n):
    for j in range(n):
        ele = int(input())
        matrix.append(ele)
matrix = np.array(matrix)
matrix= matrix.reshape(n,n)
print("matrix is :",matrix)
determinant = np.linalg.det(matrix)
print(" the determinant is:",determinant)