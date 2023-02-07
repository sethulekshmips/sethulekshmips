import numpy as np
list1=[1,2,3]
list2=[4,5,7]
v1=np.array(list1)
v2=np.array(list2)
print(v1)
print(v2)
print("sum:",np.add(v1,v2))
print("subtract:",np.subtract(v2,v1))
print("division:",np.divide(v1,v2))
print("dot:",np.dot(v1,v2))
print("cross:",np.cross(v1,v2))