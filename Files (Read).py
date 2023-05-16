"""
Modes:
"r"- read file  - Default
"w" - Write to file
"t" = text mode - Default
"b" - Binary mode
"a" = Add more content
"x" - Creates file if not exists
"+" - Read and Write
"""
f = open("Pramod.txt","rt")
content = f.read()
print(content)
# content = f.read(3)    reads the next part of the content
# print(content)
# for line in f:         For reading line by line in file
#     print(line,end="")
# print(f.readline())    Also used for reading line in file
#print(f.readline(),end="")
#print(f.readlines())     Used for reading all the lines in a list
f.close()