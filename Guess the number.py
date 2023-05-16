n = 18
count=1

for i in range (1,10):
    a = int(input())
    if(a==n):
        print("You Won!")
        print("You took ",count,"Guesses to finish")
    else:
        if (count == 9):
            print("Game Over")
            break;
        print("Wrong guess")
        print((9-count),"guesses left")
        count = count + 1


