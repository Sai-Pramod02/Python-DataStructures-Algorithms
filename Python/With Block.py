with open("Pramod.txt", 'r+') as f:  #Opens and closes automatically
    print(f.readlines())
    f.write("Helloooooo")