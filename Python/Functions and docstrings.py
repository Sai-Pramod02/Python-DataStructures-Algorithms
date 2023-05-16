a = int(input())
b = int(input())

sum1 = sum((a,b)) #Inbuilt Functions
print("Sum of " ,a,b," is :",sum1)
#User Defined Functions
def avg(a,b):
    """This function returns the average of two numbers"""
    result = (a+b)/2
    return result
print(avg.__doc__)
print("The average is :",avg(a,b))

def percentage(a,b):
    """This function return the percentages of two numbers"""
    aresult = a/100
    bresult = b/100
    return aresult,bresult
print(percentage.__doc__)
print("The percentages of a and b are ",percentage(a,b))