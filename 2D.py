import numpy as np

arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr3)
print(arr3.ndim)

arr2 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(arr2)
print(arr2.ndim)

arr = np.array([1,2,3,4],ndmin=10)
print(arr)
print(arr.ndim)


