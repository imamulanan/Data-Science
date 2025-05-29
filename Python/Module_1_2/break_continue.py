a=[1,2,3,4,5,'a',6,7,8]

for i in a:
    if type(i)==type('b'):
        break # means stop it
    else:
        print(i)
print('----')
      


a=[1,2,3,4,5,'a',6,7,8]

for i in a:
    if type(i)==type('b'):
        continue # means skip it
    else:
        print(i)        