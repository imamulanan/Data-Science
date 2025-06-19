# scope --> a region where a variable is accessible

x=10 #global variable 

print(x)

def func():
    y=19 # local variable
    print("y",y)

func() 
print("----")   

# LEGB
#L = LOCAL
#E = ENCLOSING
#G = GLOBAL
#B = BUILT in scope(print,sum,max,input)

n = "global" # Global variable

def outer():
    n="enclosing" #Enclosing variable
    def inner():
        n="Local" #local variable
        print(n)
    inner()
    print(n)
outer()
print(n)    
print("-----")    

n = "global" # Global variable

def outer():
    n="enclosing" #Enclosing variable
    def inner():
        global n  #global variable sudhu global variable k change krte pare.enclosing variable k change krte pare nah
        n="Local" #local variable
        print(n)
    inner()
    print(n)
outer()
print(n)  

print("------")

def outer():
    n="enclosing" #Enclosing variable
    def inner():
        nonlocal n #enclosing k change kre felse
        n="Local" #local variable
        print(n)
    inner()
    print(n)
outer()
print(n)  

# global-->global variable sudhu global variable k change krte pare.enclosing variable k change krte pare nah
# nonlocal---> enclosing k change kre felse, global k pare nah