# { }
# key value pair
# indexing er shujog nai
# key gula obossoi immutable

a={'Rahim' : 12, 'Karim' : 14 ,'Fahim': 78, 1:[1,2,3,4,5], 2:{3,4,5}}

# print(type(a))

for i in a:
    print(i)
print("----")

for i in a.values():
    print(i)

print(a.keys(),a.values()) #keys and values sob diya dibe    

print('-----')

for k,v in a.items():
    print(f"Key Name: {k}, Values {v}") #  key name and value aksathe dibe

a=[1,2,3]
b=["Mango","Banana","Apple"]

# {1:"Mango",  2:"Banana",.....}

print(dict(zip(a,b)))