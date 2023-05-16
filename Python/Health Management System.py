def dateTime():
    import datetime
    return datetime.datetime.now()
with open("PramodHMS_Exercises.txt", 'w') as f:
    f.write("Bench Press\n")
    f.write("Inclined Bech Press\n")
    f.write("Dumbell Press\n")
    f.write("Cable Cross Over\n")
with open("PramodHMS_Diet.txt", "w") as f:
    f.write("Bread and Peanut Butter\n")
    f.write("Milkshake\n")
    f.write("Lunch consisting of high protein\n")
    f.write("Banana and watermelon\n")
    f.write("Protein Shake\n")
with open("RiyaHMS_Exercises.txt", 'w') as f:
    f.write("Situps\n")
    f.write("Bicep Curls\n")
    f.write("Concentration curls\n")
    f.write("EZ Bar curls\n")
with open("RiyaHMS_Diet.txt", "w") as f:
    f.write("Oats\n")
    f.write("Milkshake\n")
    f.write("Lunch consisting of high protein\n")
    f.write("Banana and watermelon\n")
    f.write("Protein Shake\n")

while(True):
    print("1-Pramod\n2-Riya")
    choice = int(input())
    if(choice==1):
        print("1-Exercises\n2-Diet")
        mode = int(input())
        if(mode==1):
            with open("PramodHMS_Exercises.txt") as f:
                content = f.read()
                print(content)
        elif(mode==2):
            with open("PramodHMS_Diet.txt") as f:
                content = f.read()
                print(content)
    elif(choice==2):
        print("1-Exercises\n2-Diet")
        rmode = int(input())
        if(rmode==1):
            with open("RiyaHMS_Exercises.txt") as f:
                content = f.read()
                print(content)
        elif(rmode==2):
            with open("RiyaHMS_Diet.txt") as f:
                content = f.read()
                print(content)