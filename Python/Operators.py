#Arithematic Operators
print(5%6)
print(15//6)
x = 5
x+=7
print(x)
y = 6
#Comparision Operators
if(x%2==0 and y%2==0):
    print("Both X and Y are even")
elif(x%2!=0 and y%2==0):
    print("Only Y is even")
elif(x%2==0 and y%2!=0):
    print("Only X is even")
else:
    print("Both are not even")

#Membership Operators
L1 = [1,4,3,5,6,8,4]
print(3 in L1)
print(324 in L1)
#Bitwise Operators
print(0 & 1)
print(0 | 1)
