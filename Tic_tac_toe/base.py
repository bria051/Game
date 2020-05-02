from Game.Tic_tac_toe.choose import choosing
from Game.Tic_tac_toe.board import game_board
from Game.Tic_tac_toe.player import user_time
from Game.Tic_tac_toe.computer import empty_cells
from Game.Tic_tac_toe.winnig import w_win
from Game.Tic_tac_toe.draw_game import Draw
from pygame import *
from Game.Tic_tac_toe.map import get_number_from_pos, play_mode
from Game.Tic_tac_toe.first_attack import ran


window_width = 800
window_height = 500
board_width = 500
bg_color = (128, 128, 128)
fps = 90
fps_clock = pygame.time.Clock()

board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
win = [[0, 1, 2], [0, 4, 8], [2, 4, 6], [3, 4, 5],
       [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]

user,computer = choosing()


turn = 'user'

print("user %s, computer %s"%(user,computer))

print("%s's turn"%(turn))


pygame.init()
surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Omok Game")
surface.fill(bg_color)
draw_game = Draw(surface)
draw_game.init_game()
draw_game.draw_font()
draw_game.draw_font_t()

while(True):
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            print(event.pos)
            n, m = event.pos
            mode = play_mode(n,m)
            print("mode", mode)
            if(mode == 1):
                just = 0
                while (True):

                    depth = len(empty_cells(board))
                    vitual = w_win(board, user, computer, win)
                    if (vitual != 0):
                        game_board(board)
                        break
                    else:
                        if (turn == 'user'):
                            for event in pygame.event.get():
                                if event.type == MOUSEBUTTONUP:
                                    print(event.pos)
                                    a, b = event.pos
                                    number = get_number_from_pos(a, b)
                                    print(number)
                                    flag, board = user_time(board, number, user)
                                    if (flag != True):
                                        continue
                                    else:
                                        draw_game.draw_stone(number, user)

                                    turn = 'computer'
                        elif (turn == 'computer'):

                            for event in pygame.event.get():
                                if event.type == MOUSEBUTTONUP:
                                    print(event.pos)
                                    a, b = event.pos
                                    number = get_number_from_pos(a, b)
                                    print(number)
                                    flag, board = user_time(board, number, computer)
                                    if (flag != True):
                                        continue
                                    else:
                                        draw_game.draw_stone(number, computer)
                                    turn = 'user'
                    pygame.display.update()
                    fps_clock.tick(fps)
            elif(mode == 2):
                just = 0
                while (True):

                    depth = len(empty_cells(board))
                    vitual = w_win(board, user, computer, win)
                    if (vitual != 0):
                        game_board(board)
                        break
                    else:
                        if (turn == 'user'):
                            for event in pygame.event.get():
                                if event.type == MOUSEBUTTONUP:
                                    print(event.pos)
                                    a, b = event.pos
                                    number = get_number_from_pos(a, b)
                                    print(number)
                                    flag, board = user_time(board, number, user)
                                    if (flag != True):
                                        continue
                                    else:
                                        draw_game.draw_stone(number, user)

                                    turn = 'computer'
                        elif (turn == 'computer'):

                            rand = ran(board)
                            draw_game.draw_stone(rand, computer)
                            board[rand] = computer
                            game_board(board)

                            print('========')
                            turn = 'user'
                    pygame.display.update()
                    fps_clock.tick(fps)
            else:
                continue
        pygame.display.update()
        fps_clock.tick(fps)


"""
just = 0
while(True):

    depth = len(empty_cells(board))
    vitual = w_win(board,user,computer,win)
    if (vitual != 0):
        game_board(board)
        break
    else:
        if(turn == 'user'):
            For event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    print(event.pos)
                    a,b = event.pos
                    number = get_number_from_pos(a,b)
                    print(number)
                    flag, board = user_time(board, number, user)
                    if(flag != True):
                        continue
                    else:
                        draw_game.draw_stone(number, user)

                    turn = 'computer'
        elif(turn == 'computer'):

            rand = ran(board)
            draw_game.draw_stone(rand, computer)
            board[rand] = computer
            game_board(board)

            print('========')
            turn = 'user'


    pygame.display.update()
    fps_clock.tick(fps)
    just += 1
"""

"""
    depth = len(empty_cells(board))
    vitual = w_win(board,user,computer,win)
    if (vitual != 0):
        game_board(board)
        break
    elif (just == 9):
        print("draw")
        break
    else:
        if(turn == 'user'):
            game_board(board)
            user_time(user, board)
            turn = 'computer'
        else:
            if(depth == 9):
                loaction = random.randrange(0,3)
            else:
                move = minmax(board, depth, turn, user, computer, board, win)
                print(move)
                board[move[0]] = computer
                game_board(board)

            print('========')
            turn = 'user'

"""