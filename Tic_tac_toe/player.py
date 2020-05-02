def user_time(board, number, user):
    if(number == 100):
        return (False, board)
    else:
        if (board[number] == '*'):
            board[number] = user
            return (True, board)
        else:
            print("You cant put here. Choose again")
            return (False, board)