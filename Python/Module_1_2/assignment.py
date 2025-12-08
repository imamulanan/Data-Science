#Problem: 0

# Write a Python program that takes a number as input and checks whether it is even or odd.

a=input("Please input a number: ")

if int(a) % 2==0:
    print(a,"is even")
else:
    print(a,"is odd")   


# Problem: 02

#  Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation.

b=int(input("Please input a number: "))
c=int(input("Please input another number: "))
d=input("Please input a operator: ")

if d=='+':
    result=b+c
elif d=='-':
    result=b-c
elif d=='*':
    result=b*c
elif d=='/':
    if c!=0:
        result=b/c
    else:result = 'Error'
else:
    result='Invalid number'


print(result)                        

# Problem: 03

# Write a program using a for loop that calculates the sum of even numbers between 1 and 100.     
result=0
for i in range(2,101,2):
    result +=i

print("Sum of even numbers = ",result)    
    
