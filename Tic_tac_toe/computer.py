from math import inf as infinity
from Game.Tic_tac_toe.winnig import w_win

def check_game(mark,board,win):
    for x in range(8):
        vitual_h = 0
        for y in range(3):
            if(board[win[x][y]] == mark):
                vitual_h += 1
        if(vitual_h == 3):
            return True
    return False


def evaluate(user,computer,board,win):
    if (check_game(computer,board,win)):
        score = -1
    elif (check_game(user,board,win)):
        score = -1
    else:
        score = 0
    return score

def empty_cells(board):
    cells = []
    for i, y in enumerate(board):
        if(y == '*'):
            cells.append(i)
    return cells

def minmax(state, depth, player,user,computer,board,win):

    if player == "computer":
        best = [-1, -infinity]
    else:
        best = [-1, +infinity]
    if depth == 0 or w_win(board,user,computer,win):
        score = evaluate(user,computer,board,win)
        return [-1, score]

    for cell in empty_cells(board):
        location = cell

    if(player == "computer"):
        mark = computer
    else:
        mark = user

    board[location] = mark

    if(player == "computer"):
        player = "user"
    else:
        player = "computer"

    score = minmax(state, depth -1, player,user,computer,board,win)
    board[location] = "*"
    score[0] = location

    if player == "computer":
        if(score[1] > best[1]):
            best = score
    else:
        if(score[1] < best[1]):
            best = score

    return best