# Zero

import numpy as np

arr_zero = np.zeros(4) # 4 ta value sob zero hobe
print(arr_zero)

arr_zero1 = np.zeros((3,4))
print(arr_zero1)

# One's

arr_one = np.ones(4)
print(arr_one)

arr_one1 = np.ones((3,4))
print(arr_one1)

# Full empty array

arr_emp = np.empty(4)
print(arr_emp) # previous jeta thakbe setai show korbe 

# Range

arr_ren = np.arange(4)
print(arr_ren)


# Diagonal

arr_dia = np.eye(10)
print(arr_dia)
print("------")

# Linspace

arr_line = np.linspace(1,10,num=5)
print(arr_line)

arr_line2 = np.linspace(0,20,num=5)
print(arr_line2)
