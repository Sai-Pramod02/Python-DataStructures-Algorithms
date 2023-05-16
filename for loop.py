List1 = [1,3,5,7,"hello","World"]
for item in List1:
    print(item)
List2 = [["Harry",1],["Carry",2],["Parry",3],["Marrry",4]]
for items,lolipops in List2:
    print(items,lolipops)

dict1 = dict(List2.copy())
for items,lolipops in dict1.items():
    print(items , lolipops)
for keys in List1:
    if str(keys).isnumeric() and keys>6:
        print(item)
