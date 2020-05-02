def make_board(a):
    board = []
    for x in range(a):
        board.append([])
        for y in range(a):
            board[x].append("*")

    num = int(len(board)/2-1)
    board[num][num] = "O"
    board[num][num+1] = "X"
    board[num+1][num] = "X"
    board[num+1][num+1] = "O"

    return board


def width_change(board, mark, num):
    for x in range(len(board[num])):
        if(board[num][x] != '*' and board[num][x] != mark):
            board[num][x] = mark
def height_change(board, mark, num):
    for x in range(len(board[num])):
        if(board[x][num] != '*' and board[x][num] != mark):
            board[x][num] = mark

def width(board):
    for x in range(len(board)):
        num = 0
        front = 0
        back = 1
        blank = ['*', '*']
        while num <= len(board)-1:
            if(front != back):
                if(blank[0] == '*'):
                    if(board[x][num] == 'O'):
                        blank[0] = 'O'
                        front = num
                    elif (board[x][num] == 'X'):
                        blank[0] = 'X'
                        front = num
                if(blank[1] == '*'):
                    if(board[x][3-num] == 'O'):
                        blank[1] = 'O'
                        back = 3-num
                    elif(board[x][3-num] == 'X'):
                        blank[1] = 'X'
                        back = 3-num
            num += 1
        if(blank[0] != '*' and blank[0] == blank[1]):
            width_change(board, blank[0], x)
            return board
def height(board):
    for x in range(len(board[0])):
        num = 0
        front = 0
        back = 1
        blank = ['*', '*']
        while num <= len(board[0])-1:
            if (front != back):
                if(blank[0] == '*'):
                    if(board[num][x] == 'O'):
                        blank[0] = 'O'
                    elif (board[num][x] == 'X'):
                        blank[0] = 'X'
                if(blank[1] == '*'):
                    if(board[3-num][x] == 'O'):
                        blank[1] = 'O'
                    elif(board[3-num][x] == 'X'):
                        blank[1] = 'X'
            num += 1
        if(blank[0] != '*' and blank[0] == blank[1]):
            height_change(board, blank[0], x)
            return board

blank = ["*", "O", "X", "X", "X", "O"]

def search(blank):
    key = 0
    num = 0
    zero = 0
    list = []
    judgment = True

    while judgment:

        if key == 0:
            if zero == len(blank):
                break
            else:
                for x in range(zero + 1, len(blank)):
                    if blank[x] != "*":
                        num = x
                        key = 1
                        list.append(num)
                        break

        if key == 1:
            if len(list) <= 1:
                if num <= len(blank) - 1 and blank[num] != "*":
                    num += 1
                else:
                    list.append(num - 1)
                    key = 2

        if key == 2:
            if list[1] + 1 - list[0] >= 3 and blank[list[0]] == blank[list[1]]:
                for x in range(list[0], list[1] + 1):
                    if (blank[list[0]] == "O"):
                        if (blank[x] == "X"):
                            print("gfg")
                            judgment = False
                            break

                    if (blank[list[0]] == "X"):
                        if (blank[x] == "O"):
                            print("gg")
                            judgment = False
                            break

            else:
                key = 0
                zero = list[1]
                list = []
                num = 0
search(blank)

