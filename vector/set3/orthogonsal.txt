import numpy as np

def matrixmul(A,B):
    result = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j]=result[i][j]+A[i][k]*B[k][j]
    return result


def createidentity(rows, col):
    result = []
    for i in range(rows):
        row = []
        for j in range(col):
            if i == j:
                element = 1
            else:
                element = 0
            row.append(element)
        result.append(row)
    return np.array(result)


def transpose(matrix):
    result = []
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        row2 = []
        for j in range(col):
            element = matrix[j][i]
            row2.append(element)
        result.append(row2)

    return result

matrix = np.array([
    [1 / 3, 2 / 3, -2 / 3],
    [-2 / 3, 2 / 3, 1 / 3],
    [2 / 3, 1 / 3, 2 / 3]])

print("\nMatrix (Q) = :")
for row in matrix:
    print(row)

transpose = np.array(transpose(matrix))

print("\nTranspose Matrix (QT) = :")
for row in transpose:
    print(row)

rows = len(matrix)
cols = len(matrix[0])
identitymatrix = createidentity(rows, cols)

QQT = matrixmul(matrix, transpose)
print(f"\nQ QT = :")

for row in QQT:
    print(row)

QTQ = matrixmul(transpose, matrix)
print(f"\nQT Q = :")

for row in QTQ:
    print(row)

print("\nQ QT = QT Q = I =: ")
for row in identitymatrix:
    print(row)
