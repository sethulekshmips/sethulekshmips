import numpy as np
from scipy.sparse import csr_matrix
A = np.array([[1, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 1],
 [0, 0, 0, 2, 0, 0]])
print("Dense matrix representation: \n", A)
S = csr_matrix(A)
print("Sparse matrix: \n",S)
B = S.todense()
print("Dense matrix: \n", B)