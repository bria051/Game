# 판의 크기 3 X 3
size = 3
board = [['*' for _ in range(size)] for _ in range(size)]

# 돌을 뒀을 때 승부가 났는지 판가름함
def select(a, b, color):
    # 연속해야 하는 돌의 갯수
    rock = 3

    scores = [0, 0, 0, 0]
    flag = [['O', 'O'] for _ in range(4)]

    for i in range(1, rock):

        # scores[0]
        if flag[0][0] == 'O':
            if a + i < size:
                if board[a+i][b] == color:
                    scores[0] += 1
                else:
                    flag[0][0] = 'X'
            else:
                flag[0][0] = 'X'
        if flag[0][1] == 'O':
            if a - i >= 0:
                if board[a-i][b] == color:
                    scores[0] += 1
                else:
                    flag[0][1] = 'X'
            else:
                flag[0][1] = 'X'

        # scores[1]
        if flag[1][0] == 'O':
            if b + i < size:
                if board[a][b+i] == color:
                    scores[1] += 1
                else:
                    flag[1][0] = 'X'
            else:
                flag[1][0] = 'X'
        if flag[1][1] == 'O':
            if b - i >= 0:
                if board[a][b-i] == color:
                    scores[1] += 1
                else:
                    flag[1][1] = 'X'
            else:
                flag[1][1] = 'X'

        # scores[2]
        if flag[2][0] == 'O':
            if a + i < size and b + i < size:
                if board[a+i][b+i] == color:
                    scores[2] += 1
                else:
                    flag[2][0] = 'X'
            else:
                flag[2][0] = 'X'
        if flag[2][1] == 'O':
            if a - i >= 0 and b - i >= 0:
                if board[a-i][b-i] == color:
                    scores[2] += 1
                else:
                    flag[2][1] = 'X'
            else:
                flag[2][1] = 'X'

        # scores[3]
        if flag[3][0] == 'O':
            if a - i >= 0 and b + i < size:
                if board[a-i][b+i] == color:
                    scores[3] += 1
                else:
                    flag[3][0] = 'X'
            else:
                flag[3][0] = 'X'
        if flag[3][1] == 'O':
            if a + i < size and b - i >= 0:
                if board[a+i][b-i] == color:
                    scores[3] += 1
                else:
                    flag[3][1] = 'X'
            else:
                flag[3][1] = 'X'

    total = True if max(scores) == rock - 1 else False

    return total

# 돌을 두는 자리가 빈 자리인지 확인
def place(color):
    while True:
        player = int(input("choose 1~{}: ".format(size ** 2)))
        if player > 0 and player < size ** 2 + 1:
            player -= 1
            if board[int(player / size)][player % size] == '*':
                board[int(player / size)][player % size] = color
                break
            else:
                print("you can't put here. choose again")
        else:
            print("wrong number")

    return int(player / size), player % size

# 판을 출력
def print_board():
    sentence = ""
    for x in range(len(board)):
        for y in board[x]:
            sentence += y
            sentence += " "
        sentence += "\n"
    print(sentence)

player1 = 'O'
player2 = 'X'
turn = player1
count = 0

while True:
    print('\n')
    print_board()
    if turn == player1:
        print("player1's turn")
        a, b = place(turn)
        final = select(a, b, turn)
        if final:
            print_board()
            print('player1 win!!')
            break
        else:
            turn = player2

    else:
        print("player2's turn")
        a, b = place(turn)
        final = select(a, b, turn)
        if final:
            print_board()
            print('player2 win!!')
            break
        else:
            turn = player1

    count += 1
    if count == size**2:
        print('\n')
        print_board()
        print('draw')
        break
