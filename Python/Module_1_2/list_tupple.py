# s="Hello"
# print(list(s))

s=['Hello']

s.append(['World']) #  append list er akta function
print(s)

s.reverse() # reverse kore

print(s)


#tuple() immutable

t=(1,2,3)
# t[0]=100  
# print(t) kaj korbe nah cz immutable

t_r=tuple(reversed(t))

print(t)
print(t_r)