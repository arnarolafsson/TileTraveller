x,y = 1,1


while (x,y != 3,1):
    if (x == 1 and y == 1):
        print("You can travel: (N) orth.")
        direct = input("Direction: ").lower()
        if direct == "n":
            y = y + 1
        else:
            print("Not a valid direction!")

    if (x == 2 and y == 1):
        print("You can travel: (N) orth.")
        direct = input("Direction: ").lower()
        if direct == "n":
            y = y + 1
        else:
            print("Not a valid direction!")

    if (x == 3 and y == 1):
        print("Victory!")
        break
    if (x == 1 and y == 2):
        print("You can travel: (N) orth or (E) ast or (S) outh")
        direct = input("Direction: ").lower()
        if direct == "n":
            y = y + 1
        elif direct == "e":
            x = x + 1
        elif direct == "s":
            y = y - 1
        else:
            print("Not a valid direction!")
 
    if (x == 2 and y == 2):
        print("You can travel: (S) outh or (W)est.")
        direct = input("Direction: ").lower()
        if direct == "s":
            y = y - 1
        elif direct == "w":
            x = x - 1
        else:
            print("Not a valid direction!")

    if (x == 3 and y == 2):
        print("You can travel: (N) orth or (S) outh.")
        direct = input("Direction: ").lower()
        if direct == "n":
            y = y + 1
        elif direct == "s":
            y = y - 1
        else:
            print("Not a valid direction!")

    if (x == 1 and y == 3):
        print("You can travel: (E) ast or (S) outh")
        direct = input("Direction: ").lower()
        if direct == "e":
            x = x + 1
        elif direct == "s":
            y = y - 1
        else:
            print("Not a valid direction!")

    if (x == 2 and y == 3):
        print("You can travel: (E) ast or (W) est")
        direct = input("Direction: ").lower()
        if direct == "e":
            x = x + 1
        elif direct == "w":
            x = x - 1
        else:
            print("Not a valid direction!")

    if ( x == 3 and y == 3):
        print("You can travel: (W) est or (S) outh")
        direct = input("Direction: ").lower()
        if direct == "w":
            x = x - 1
        elif direct == "s":
            y = y - 1
        else:
            print("Not a valid direction!")

    
            
