row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]

def clearBoard():
    global row1
    global row2
    global row3
    row1 = [" "," "," "]
    row2 = [" "," "," "]
    row3 = [" "," "," "]

def showBoard():
    print ("   |   |   ")
    print (" " + row1[0] + " | " + row1[1] + " | " + row1[2])
    print ("   |   |   ")
    print ("---+---+---")
    print ("   |   |   ")
    print (" " + row2[0] + " | " + row2[1] + " | " + row2[2])
    print ("   |   |   ")
    print ("---+---+---")
    print ("   |   |   ")
    print (" " + row3[0] + " | " + row3[1] + " | " + row3[2])
    print ("   |   |   ")

def win():
    if (row1[0] == row2[1] == row3[2] == "X"):
        print ("X wins!")
        return True
    elif (row1[0] == row2[1] == row3[2] == "O"):
        print ("O wins!")
        return True
    if (row1[2] == row2[1] == row3[0] == "X"):
        print ("X wins!")
        return True
    elif (row1[2] == row2[1] == row3[0] == "O"):
        print ("O wins!")
        return True
    elif (row1[0] == row2[0] == row3[0] == "O"):
        print ("O wins!")
        return True
    elif (row1[0] == row2[0] == row3[0] == "X"):
        print ("X wins!")
        return True
    elif (row1[1] == row2[1] == row3[1] == "X"):
        print ("X wins!")
        return True
    elif (row1[2] == row2[2] == row3[2] == "X"):
        print ("X wins!")
        return True
    elif (row1[1] == row2[1] == row3[1] == "O"):
        print ("O wins!")
        return True
    elif (row1[2] == row2[2] == row3[2] == "O"):
        print ("O wins!")
        return True
    elif (row1 == ["O","O","O"] or row2 == ["O","O","O"] or row3 == ["O","O","O"]):
        print ("O wins!")
        return True
    elif (row1 == ["X","X","X"] or row2 == ["X","X","X"] or row3 == ["X","X","X"]):
        print ("X wins!")
        return True
    else:
        return False

def full(row, column):
    if (row[column] != " "):
        return True
    else:
        return False

def insert(row,column,letter):
    row[column] = letter
    print("OK, I've put an " + letter + " in that spot")

def play():
    clearBoard()
    print ("Let's play Tic Tac Toe!")
    while (not win()):
        showBoard()
        pos = input("X, which spot would you like to pick? ")
        while (4 == 4):
            if pos.lower() == "center" or pos.lower() == "middle":
                if not full(row2,1):
                    insert(row2,1,"X")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "top-right" or pos.lower() == "topright" or pos.lower() == "top right":
                if not full(row1,2):
                    insert(row1,2,"X")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "top-left" or pos.lower() == "topleft" or pos.lower() == "top left":
                if not full(row1,0):
                    insert(row1,0,"X")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "top-center" or pos.lower() == "topcenter" or pos.lower() == "top middle" or pos.lower() == "top-middle" or pos.lower() == "topmiddle" or pos.lower() == "top center":
                if not full(row1,1):
                    insert(row1,1,"X")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "center-right" or pos.lower() == "centerright" or pos.lower() == "center right" or pos.lower() == "middle-right" or pos.lower() == "middleright" or pos.lower() == "middle right":
                if not full(row2,2):
                    insert(row2,2,"X")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "center-left" or pos.lower() == "centerleft" or pos.lower() == "center left" or pos.lower() == "middle-left" or pos.lower() == "middleleft" or pos.lower() == "middle left":
                if not full(row2,0):
                    insert(row2,0,"X")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "bottom-right" or pos.lower() == "bottomright" or pos.lower() == "bottom right":
                if not full(row3,2):
                    insert(row3,2,"X")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "bottom-left" or pos.lower() == "bottomleft" or pos.lower() == "bottom left":
                if not full(row3,0):
                    insert(row3,0,"X")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "bottom-center" or pos.lower() == "bottomcenter" or pos.lower() == "bottom middle" or pos.lower() == "bottom-middle" or pos.lower() == "bottommiddle" or pos.lower() == "bottom center":
                if not full(row3,1):
                    insert(row3,1,"X")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            else:
                print("Sorry, I couldn't understand.")
                pos = input("Try again. Which spot would you like to pick? ")
        showBoard()
        if (win()):
            break;
        elif (" " not in row1 and " " not in row2 and " " not in row3):
            print("Draw!")
            break;
        pos = input("O, which spot would you like to pick? ")
        while (4 == 4):
            if pos.lower() == "center" or pos.lower() == "middle":
                if not full(row2,1):
                    insert(row2,1,"O")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "top-right" or pos.lower() == "topright" or pos.lower() == "top right":
                if not full(row1,2):
                    insert(row1,2,"O")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "top-left" or pos.lower() == "topleft" or pos.lower() == "top left":
                if not full(row1,0):
                    insert(row1,0,"O")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "top-center" or pos.lower() == "topcenter" or pos.lower() == "top middle" or pos.lower() == "top-middle" or pos.lower() == "topmiddle" or pos.lower() == "top center":
                if not full(row1,1):
                    insert(row1,1,"O")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "center-right" or pos.lower() == "centerright" or pos.lower() == "center right" or pos.lower() == "middle-right" or pos.lower() == "middleright" or pos.lower() == "middle right":
                if not full(row2,2):
                    insert(row2,2,"O")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "center-left" or pos.lower() == "centerleft" or pos.lower() == "center left" or pos.lower() == "middle-left" or pos.lower() == "middleleft" or pos.lower() == "middle left":
                if not full(row2,0):
                    insert(row2,0,"O")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "bottom-right" or pos.lower() == "bottomright" or pos.lower() == "bottom right":
                if not full(row3,2):
                    insert(row3,2,"O")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "bottom-left" or pos.lower() == "bottomleft" or pos.lower() == "bottom left":
                if not full(row3,0):
                    insert(row3,0,"O")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            elif pos.lower() == "bottom-center" or pos.lower() == "bottomcenter" or pos.lower() == "bottom middle" or pos.lower() == "bottom-middle" or pos.lower() == "bottommiddle" or pos.lower() == "bottom center":
                if not full(row3,1):
                    insert(row3,1,"O")
                    break;
                else:
                    print("That space is occupied.")
                    pos = input("Try again. Which spot would you like to pick? ")
            else:
                print("Sorry, I couldn't understand.")
                pos = input("Try again. Which spot would you like to pick? ")
    win()
    again = input("Do you want to play again (y/n)? ")
    if (again == "y"):
        clearBoard()
        play()
    elif (again == "n"):
        print ("Ok, alright.")
    else:
        print ("I asked for y or n.")
        again = input("Try again. Do you want to play again (y/n)? ")
play()
