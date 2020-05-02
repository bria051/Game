import random

a = int(input())
class Board:

    def __init__(self):
        self.board = []
        self.box = []
        self.number = []
        self.num = 0
        self.count = 0
        self.ber = 0
        self.sentence = ""

    # back_side는 공백리스트, board는 num_list이다.
    def make_board(self, a):
        # board는 판, box와 number는 board에 넣을 수를 랜덤으로 고르기 위하 사용하는 리스트이다.
        board = self.board
        box = self.box
        number = self.number
        num = self.num
        count = self.count

        # 만들 board의 길이만큼 수를 number에 만들어 넣음.
        for x in range(int(a*a/2)*2):
            number.append("%d" %(num+1))
            count += 1
            if count == 2:
                num += 1
                count = 0

        # number에 만든 수를 랜덤으로 섞어서 board에 넣음.
        while len(board) != len(number):
            ber = 0
            n = random.randrange(len(number))
            for y in box:
                if y == n:
                    ber += 1
            if ber == 0:
                board.append(number[n])
                box.append(n)

        back_side = []
        for x in range(len(board)):
            back_side.append('*')

        # 수가 섞인 board와 공백리스트를 내보냄.
        return back_side, board

    def print_board(self, a, board):
        # board를 가로 a 세로 a로 출력
        self.num = len(board)
        num = self.num
        ber = self.ber
        sentence = self.sentence
        for x in range(num):
            if ber != a:
                sentence += board[x]
                if ber != a - 1:
                    sentence += " "
                ber += 1
            if ber == a and x != num-1:
                sentence += "\n"
                ber = 0
        print(sentence)

b = Board()
board, num_list = b.make_board(a)
b.print_board(a, board)