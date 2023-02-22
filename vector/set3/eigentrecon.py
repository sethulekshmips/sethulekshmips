from numpy import diag
import numpy as np
from numpy import dot
from numpy.linalg import inv
from numpy.linalg import eig

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("\nMatrix = :")
for row in matrix:
    print(row)
Evalues, Evectors = eig(matrix)
invEig = inv(Evectors)
Diagfrmvect = diag(Evalues)
rematrix = Evectors.dot(Diagfrmvect).dot(invEig)

print("\nRe-Constructed Matrix = :")
for row in rematrix:
    print(row)