import random

def first_attack():
    a = random.randrange(0,2)
    if (a == 0):
        user = 'first'
        computer = 'second'
    else:
        user = 'second'
        computer = 'first'
    return user, computer

def ran(board):

    while(True):
        a = random.randrange(0,9)
        if(board[a] == '*'):
            return a