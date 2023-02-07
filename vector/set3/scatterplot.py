import matplotlib.pyplot as plt
import numpy as np

matrix = np.array([
    [5,99],[6,85],[9,88],[4,100],[8,85]]
)

x,y=np.split(matrix,2,axis=1)

plt.scatter(x, y)
plt.show()