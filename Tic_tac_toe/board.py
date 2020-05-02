def game_board(board):
    for x in range(0, 9, 3):
        print(board[x], board[x + 1], board[x + 2])