import random

def mix_card(num):
    # 숫자를 입력받고 받은 수만큼, 같은 수 2개를 각각 list_n 에 넣어서 출력

    list_n = []
    count = []
    overside = []

    for x in range(int(num/2)*2):
        overside.append('*')
        if x < int(num/2):
            count.append(0)

    while len(list_n) < int(num / 2) * 2:
        n = random.randrange(1, int(num / 2) + 1)
        if count[n - 1] < 2:
            list_n.append(n)
            count[n - 1] += 1

    return list_n, overside

def print_board(board):
    # 판을 보기 편하게 출력함

    sentence = ""
    for x in range(len(board)):
        if x == len(board)/2:
            sentence += "\n"
        sentence += str(board[x])
        sentence += " "
    print(sentence)

def change_board(board, overside):
    # 두개의 수를 입력받고 받은 n번째의 두 수들을 비교함

    box = []
    print_board(overside)
    for x in range(2):
        while True:
            a = int(input("choose number 1~%d: "%(len(board))))
            if a > len(board) or board[a-1] == '*':
                print("you cant choose that number")
            else:
                break

        board[a-1], overside[a-1] = overside[a-1], board[a-1]
        box.append(a)
        print_board(overside)

    if overside[box[0]-1] != overside[box[1]-1]:
        board[box[0]-1], overside[box[0]-1] = overside[box[0]-1], board[box[0]-1]
        board[box[1]-1], overside[box[1]-1] = overside[box[1]-1], board[box[1]-1]
        print("not same")
    else:
        print("same")

    return board, overside

def discriminate(board):
    # 모든 수들이 선택되면 게임을 끝내는 신호를 줌

    num = 0
    for x in board:
        if x != '*':
            return 0
        else:
            num += 1
    if num == len(board):
        return 1


board, overside = mix_card(2)
while True:
    change_board(board, overside)
    flag = discriminate(board)
    if flag == 1:
        print("game end")
        break
