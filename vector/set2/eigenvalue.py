import numpy as np

m = np.array([[1, 2, 3],
              [2, 3, 4],
              [4, 5, 6]])

print("the orginal vector:\n",m)

w, v = np.linalg.eig(m)

print("the eigenvalues:\n",w)

print("Printing Right eigenvectors of the given square array:\n",
      v)