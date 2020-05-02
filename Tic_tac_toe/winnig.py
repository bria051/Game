def w_win(board,user,computer,win):
    mt = 0
    for x in range(8):
        vitual_h = 0
        vitual_c = 0
        for y in range(3):
            if(board[win[x][y]] == user):
                vitual_h += 1
        for z in range(3):
            if(board[win[x][z]] == computer):
                vitual_c += 1
        if(vitual_h == 3):
            #print("user win!!")
            mt += 1
            break
        elif(vitual_c == 3):
            #print("computer win!!")
            mt += 1
            break
    if(mt != 0):
        return True
    return False