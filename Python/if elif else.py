num1 = [5,3,6,7]
if 3 in num1:
    print("Yes")
elif 5 not in num1:
    print("Yes")
elif 5  in num1:
    print("NO")

print("Yes") if 9 in num1 else print("No")   #Short-Hand if-else Notation
print("Present") if 3 in num1 else print("Absent")