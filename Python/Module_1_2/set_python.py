# { }
# Unordered ---> indexing kore paowa jabe nah

# immutable ----> no update
# No duplicates

a=[1,2,2,2,3,4,4,4,5]
s=set(a)
print(s)
# print(s[0]) # indexing koreow value ber kora jabe nah 


#union intersection 

b={1,2,3,4,5,6}
c={3,4,5,6,7,8}

d=b.intersection(c)
print(d)

e=b.union(c)
print(e)