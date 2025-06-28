import numpy as np

# add
v1 = np.array([1,2,3,4])

print(np.sin(v1))
print(np.cos(v1))

vadd = v1+3
print(vadd)

v2 = np.array([4,3,2,1])

v2add = np.add(v1,v2)
print(v2add)

v2mul = np.multiply(v1,v2) #v1*v2
print(v2mul)

v2div = np.divide(v1,v2) #v1/v2
print(v2div)


v3 = np.array([[1,2,3,4],[1,2,3,4]])
v4 = np.array([[1,2,3,4],[1,2,3,4]])

D2_add  = np.add(v3,v4)
print()
print(D2_add)

print("Min : ",np.min(v1),np.argmin(v1))
print("Max : ",np.max(v1),np.argmax(v1))
print("Cumsum: ",np.cumsum(v1))

var1 = np.array([[2,1,3],[9,5,6]])
print(np.min(var1,axis=1)) # axis 1 mean row
print(np.min(var1,axis=0)) # axis 0 mean coloum
 