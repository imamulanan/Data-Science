# file=open('name.txt','r')
# content = file.read()
# print(content)
# file.close()

# with open('name.txt','r') as f:
#     content=f.read()
#     print(content)

# write method

# with open('name.txt','w') as f:
    #egula dile full file muche new line add hbe 

    # f.write('Hello world\n')
    # f.write('I am writing in a file\n')    

# with open('name.txt','a') as f: # use append method
#     f.write('\nMy hall is Bijoy 24 Hall\n')
#     f.write('My blood group is O+\n')   

# lines = ['\nI love python\n', 'I am new to python\n']

# with open('name.txt','a') as f:
#     f.writelines(lines) 


# video 3.11
import os

import pathlib

if os.path.exists('name.txt'):
    print('File exists')
else:
    print('File not exist')    


file_path = pathlib.Path('name.txt')

if file_path.exists():
    print('File exists')
print(os.path.abspath('name.txt'))  
print(os.path.getsize('name.txt')) # byte e size dibe  

