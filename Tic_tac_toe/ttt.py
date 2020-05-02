n = int(input())
memory = board
for x in range(2):
    value = True
    while value:
        if board[n] != '*':
            board[n] = num_list[n]
            value = False
        else:
            print("Choose again")