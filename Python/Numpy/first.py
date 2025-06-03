import numpy as np

my_lst=[1,2,3,4,5]
arr1=np.array(my_lst)
print(type(arr1))
print(type(my_lst))
print(arr1)
print(arr1.ndim) # ndim diye bujhaay n dymansional
print(arr1.shape)

lst1=[1,2,3,4,5]
lst2=[3,4,5,6,7]
lst3=[6,5,4,3,2]

arr2=np.array([lst1,lst2,lst3])
print(arr2)
print(arr2.ndim)


import timeit

code = "[j**4 for j in range(1,9)]"
execution_time = timeit.timeit(code, number=10000)
print(f"Execution time: {execution_time:.6f} seconds")
