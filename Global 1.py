l = 20  # Global


def func1(n):
    # l=5 #Local
    m = 3
    # print(l)  #Prints the local value of l
    # print(n,"apples")
    # l=l+5  #Global l value cannot be changed  Therefore Global keyword should be present for changing the varible
    global l
    l = l + 45
    print(l, m)


func1(4)
print(l)  # Prints the global value of l
# m+l #Cannot recognize m because 'm' is a local variable
