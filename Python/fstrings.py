# Normal methods :
# 1
a = "Pramod"
b = "Pranavs Bro"
str = "This is %s" % a
print("Normal method 1 : \t", str)
# 2
str1 = "This is {} and {}".format(a,b)
print("Normal method 2 : \t", str1)
# all the normal methods are a little hard to implement and does not have a good code readability
# Therefore fstrings help to deliver these attributes
# Implementation of fstrings

c = "Pramod"
str2 = f"This is {c} {2 + 1} {'riya'}"
print(str2)
