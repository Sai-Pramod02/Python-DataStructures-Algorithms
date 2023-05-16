x = 89


def pram():
    x = 49

    def riy():
        global x  # Changes the global value of x not the value of x not the one which is in the function
        x = 50

    print("Before calling riy", x)
    riy()
    print('After calling riy', x)  # Returns the value of pram()'s x as there is no change made to local x value


pram()
print(x)  # Returns the value of 50 because globally the value of x is assigned to be 50
