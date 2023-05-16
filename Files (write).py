f = open("Riya.txt","w")
f.write("Spam and all that is aesthetic")
f.close()



f = open("Pramod.txt","a")  #Append mode - Adds text to the file
a=f.write("Riya is soo cute!!!!")
print(a) #prints the number of characters written to the file
f.close()


f = open("Riya.txt","r+")  #Read and write mode
print(f.read())
f.write("\nI love Pramod!!!")
f.close()




