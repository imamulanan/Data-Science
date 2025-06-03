# marks = int(input('Enter the marks: '))

# if marks >=90 and marks<=100:
#     print("Your grade is: A")
# elif  marks >=80 and marks<=89:
#     print("Your grade is: B") 
# elif  marks >=70 and marks<=79:
#     print("Your grade is: C")
# elif  marks >=60 and marks<=69:
#     print("Your grade is: D") 
# elif  marks >=50 and marks<=59:
#     print("Your grade is: E") 
# elif  marks >=40 and marks<=49:
#     print("Your grade is: E-")
# elif  marks>100 :
#     print("Please give number from 0-100 ")     
# else:
#     print("F or Fail")                          


i =0
while i<10:
    result = int(input("Enter your marks: "))
    if result>100:
        print("please write your right marks : ")
        i= i + 1
    else:
        break

if(100>= result >=90):
    print("Your grade is: A")
elif(89>= result >=80):
    print("Your grade is: B")
elif(79>= result >=70):
    print("Your grade is: C")
elif(69>= result >=60):
    print("Your grade is: D")
elif(59>= result >=50):
    print("Your grade is: E")
elif(49>=result>=40):
    print("Your grade is: E-")
else:
    print("Your grade is: F or Fail")