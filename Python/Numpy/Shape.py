import numpy as np

var = np.array([[1,2],[1,2]])

print(var)
print()
print(var.shape)

var2 = np.array([1,2,3,4], ndmin=4)

print(var2)

print(var2.shape)

# reshape:

v = np.array([1,2,3,4,5,6])
x = v.reshape(3,2)
print(x)