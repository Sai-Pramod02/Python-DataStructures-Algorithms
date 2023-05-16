print("welcome to the game:")


print("oki, so what do wanna know?")
for i in range(3):
    print("1. where is your soulmate"
          "2. send a message to your soulmate"
          "3. surprise")
    ch = int(input())
    if ch == 1:
        print("choose:"
              "elku"
              "budhu"
              "babyku")
        n = str(input())
        if n == "elku":
            print("your soulmate is on the left")
            print("my soulmate is ku")
        elif n == "budhu":
            print("your soulmate is on the right")
            print("my soulmate is tubu")
        elif n == "babyku":
            print("your soulmate is right in front of you")

    if ch == 2:
        print("sending a message = I LOVE YOU BABY KU")
        print("    .8  8. 8. 8   8. 8 8. 8 ")
        print(" . 8         . 8         .8")
        print(".  8                     .8")
        print(".    8                 .8")
        print("  .    8            .8")
        print("     .   8         .8")
        print("         .  8 8 8")
        print("             .8")

    if ch == 3:
        print("the game is over but my love for you never end<3")
        print("love you ku")