def choosing():
    print("Choose O or X to play the Game:")
    while (True):
        user = input()

        if (user == 'O'):
            computer = 'X'
            break
        elif (user == 'X'):
            computer = 'O'
            break
        else:
            print("You chose the wrong one. Choose again")
    return user,computer
