import random

while (True):
    num = random.randint(0, 1000)
    print("You got : ", num, " rupees!")
    num1 = random.random() *100  # multiply with the maximum number you want to generate
    print("Your weight is : ", num1, "KG")
    lst = ["Riya", "Pramod", "Pranav", "Akshatha"]
    winner = random.choice(lst)
    print("The Winner is : \n", winner, "!!!")

    print("any key - Exit\n1-executing again")
    choice = int(input())
    if (choice == 1):
        continue;
    else:
        break;
