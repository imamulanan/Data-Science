a=[-10,2,19,-3,-5] #[0, 2, 19, 0, 0]

i=0

while i<len(a):
    if a[i]<0:
        a[i]=0
    i+=1    
print(a)    