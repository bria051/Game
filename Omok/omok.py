def make_board(a):
    board = []
    number = []
    num = 1
    for x in range(a):
        board.append([])
        number.append([])
        for y in range(a):
            board[x].append("*")
            if(num < 10):
                number[x].append("0"+"%d"%(num))
            else:
                number[x].append("%d"%(num))
            num += 1

    return board, number
def print_board(list):
    sentence = ""
    for x in range(len(list)):
        for y in range(len(list[x])):
            sentence += list[x][y]
            if y != len(list[x])-1:
                sentence += " "
        if x != len(list)-1:
            sentence += "\n"
    print(sentence)
board, number = make_board(7)

def check(list):
    turn = "O"
    num = 0
    for x in list:
        if x == turn:
            num += 1
        else:
            num = num
    if num == 5:
        return True
def range_select(a, board):
    width = []
    length = []
    l_cross = []
    r_cross = []

    num = 0
    while a > len(board):
        a -= len(board)
        num += 1

    b = a
    ber = num

    for x in range(len(board)):
        width.append(board[num][x])
        length.append(board[x][a])

    while num != 0 and a != 0:
        num -= 1
        a -= 1
    while ber != 0 and b != len(board)-1:
        ber -= 1
        b += 1

    while num < len(board) and a < len(board):
        l_cross.append(board[num][a])
        a += 1
        num += 1

    while ber < len(board) and b > -1:
        r_cross.append(board[ber][b])
        b -= 1
        ber += 1

    if check(width) == True or check(length) == True or check(l_cross) == True or check(r_cross):
        return True
