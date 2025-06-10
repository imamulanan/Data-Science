import functools  # for using reduce function

# anonymous function ---> unnamed
# lambda function sudhu return kore print korte pare nah

def square(x):
    return x*x

print(square(5))


# lambda arguments: expression

square=lambda x: x*x

print(square(5))

add = lambda a,b: a+b
print(add(5,6))


std=[("Anan",89),("Masum",87),("Fahim",90)]
sorted_std=sorted(std,key=lambda x:x[1])
print(sorted_std)

# important functions are map(),filter(),reduce()

# Map()

num=[1,2,3,4,5]

# sq_num=list(map(square korte cacchi, kar upor korte cacchi))

sq_num=list(map(lambda x:x*x,num))
print(sq_num)

# filter 

even = list(filter(lambda x: x%2==0,num))
print(even)


# reduce 

sum = functools.reduce(lambda x,y : x+y,num) #for print the sum

print(sum)

