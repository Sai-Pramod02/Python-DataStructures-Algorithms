def factorial_iterative(n):
    # n*(n-1)*(n-2)...1
    # n*(n-1)!
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

def factorial_recursive(n):
    if n==0:
        return 1
    else:
        return n*factorial_recursive(n-1)
def fibbonacci(n):
    #0 1 1 2 3 5 8 13
    #(n-1)+(n-2)
    if(n==1):
        return(0)
    elif(n==2):
        return(1)
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)
num = int(input("Enter your number"))
print("iterative : ",factorial_iterative(num))
print("recursive : ",factorial_recursive(num))

print("Fibbonacci series : ", fibbonacci(num))