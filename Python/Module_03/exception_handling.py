# errors vs exceptions

# compile time, Run time
#Errors ---> compile time er error
#       ---> syntax, Indentation
#Exceptions ---> Run time error
#           ---> Indexing, key, values,zero division

try: # je code e exception thakbe
    with open('rahim.txt','r') as f:
        print(f.read())
except FileNotFoundError:
    print('File not found')  



try: # je code e exception thakbe
    with open('name.txt','r') as f:
        print(f.read())
    print(10/10) # for ZeroDivisionError
    x=int('123') # for ValueError (abc/123)
    a = [1,2,3,4]
    print(a[1]) # IndexError
    z = abc # unnamed error
except ZeroDivisionError:
    print('Error: Division by zero is not possible')        
except FileNotFoundError:
    print('File not found')

except ValueError:
    print('Invalid value') 
except IndexError:
    print('Invalid Index')
except Exception as e :
    print("Some error occurred!!",e) 

# video 3.14

else:
    print('code executed successfully!!')

finally:
    print('error thak na thak, eta always print hobei ')   

# manually ekta exception trigger
# custom error baniyechi

def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError('Only .txt files are allowed ') 
    print('Valid File ')

check_file('data.txt')

# video 3.15
# custom error handling

try:
    check_file('data.csv')
except Exception as e:
    print(e)    
