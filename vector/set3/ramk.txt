import numpy as np
a = np.array([ [1,2,3] ,[6,7,8], [2,4,6] ])
rank = np.linalg.matrix_rank(a)
print("the matrix is:",a)
print("rank of the matrix is:",rank)