f = open("Pramod.txt")
print(f.readline())
print("The file pointer is at : ", f.tell())  #Returning the position of file pointer
print(f.readline())
f.seek(0) #Placement of file pointer
print("The file pointer is at :", f.tell())
print(f.readline())
f.close()