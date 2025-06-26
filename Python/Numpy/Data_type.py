import numpy as np

var = np.array([1,2,3,4,5,6,7])

print("Data types: ",var.dtype)

var1 = np.array([1.0,1.5,2.6])

print("Data types: ",var1.dtype)

var2 = np.array(['a','b','c'])

print("Data types: ",var2.dtype)

var3 = np.array([1,2,3,4,5,6,7],dtype=np.int64) # change the data type

print("Data types: ",var3.dtype)

var4 = np.array([1,2,3,4,5,6,7],dtype="f") # change the data type

print("Data types: ",var4.dtype)
print(var4)

var5 = np.array([1,2,3,4,5,6,7])

new_var5 = var5.astype(float)
