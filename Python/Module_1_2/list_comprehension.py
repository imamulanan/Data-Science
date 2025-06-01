# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

a=[1,10,23,24,26,90]

result=[]

for i in a:
    if i%2==0:
        result.append(i)
print(result) 

# list comprehension

new_result=[i for i in a if i%2==0]
print(new_result)


b=[1,2,3,4,5,6]  #---->[1,4,3,16,5,36]

b_new=[i**2 if i%2==0 else i for i in b ]
print(b_new)