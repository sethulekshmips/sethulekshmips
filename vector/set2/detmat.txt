import numpy as np

def determinant(mat):
    det = np.linalg.det(mat)
    return round(det)

mat = [[1, 0, 2, -1],
       [3, 0, 0, 5],
       [2, 1, 4, -3],
       [1, 0, 5, 0]]

print('Determinant of the matrix is:',
      determinant(mat))