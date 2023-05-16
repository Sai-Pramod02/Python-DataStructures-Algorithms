# def metha(a,b,c):
#     print(a,b,c)
#
# metha("Riya", "Pramod", "Pranav","Akshatha")

def meth(a,*args,**kwargs):
    for items in args:
        print(a,items)
    for items,values in kwargs.items():
        print(items,values)
        

lst = ["Riya", "Pramod", "Pranav","Akshatha"]
meth(5,*lst)
dict1 = {"Riya":"Aesthetic Model", "Pramod":"Lazy gooze", "Pranav":"Brainy guyy"}
meth(5,*lst,**dict1)


