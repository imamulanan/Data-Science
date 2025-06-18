# 2 types

# 1. user defined function ----> programmer nijer iccha moto banay

# 2. built in function ---> already banano ache




# user defined function 

# 1. No input, No output/return

def my_first_func():# function define
    a=30
    b=20
    print(a+b)

my_first_func()    # function call kora

# Input, no return

def add_two_numbers(a,b): # ekhane a,b hocche argument 
    print(a+b)


add_two_numbers(5,20) #ekhane 5,20 hocche parameters  


#has input and output/return

def multiply_two_num(a,b):
    return a*b
result = multiply_two_num(12,2)
print(result)

# No input and has output/return

def hello():
    return "Hello"

greeting = hello()
print(greeting)