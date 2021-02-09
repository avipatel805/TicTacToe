import pygame as pg
import endgame
pg.init()

screen = pg.display.set_mode([600, 600])
running = True
pg.display.set_caption('Tic Tac Toe')
board = [1, ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ']
player = False
pg.font.init()
font = pg.font.SysFont('freesansbold.ttf', 350)
x = font.render('X', False, (0, 0, 0))
o = font.render('O', False, (0, 0, 0))


def button(mouse):
    if 0 < mouse[0] < 200:
        if 0 < mouse[1] < 200:
            return 7
        elif 200 < mouse[1] < 400:
            return 4
        else:
            return 1
    if 200 < mouse[0] < 400:
        if 0 < mouse[1] < 200:
            return 8
        elif 200 < mouse[1] < 400:
            return 5
        else:
            return 2
    if 400 < mouse[0] < 600:
        if 0 < mouse[1] < 200:
            return 9
        elif 200 < mouse[1] < 400:
            return 6
        else:
            return 3
    return -1


def place(num):
    if num == 7:
        return (15, 0)
    elif num == 8:
        return (215, 0)
    elif num == 9:
        return (415, 0)
    elif num == 4:
        return (15, 200)
    elif num == 5:
        return (215, 200)
    elif num == 6:
        return (415, 200)
    elif num == 1:
        return (15, 400)
    elif num == 2:
        return (215, 400)
    elif num == 3:
        return (415, 400)
    return (-500, -500)

'''
def drawBoard(bo):
    for item in range(1, 10):
        if item ==
'''

screen.fill((255, 255, 255))
pg.draw.line(screen, (0, 0, 0), (200, 0), (200, 600))
pg.draw.line(screen, (0, 0, 0), (400, 0), (400, 600))
pg.draw.line(screen, (0, 0, 0), (0, 200), (600, 200))
pg.draw.line(screen, (0, 0, 0), (0, 400), (600, 400))
#pg.draw.rect(screen, (0, 255, 255), (0, 0, 200, 200))

click = 1
state = 'player1'
winner = ''
while running:
    mouse = (0, 0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            clicked = True
            mouse = pg.mouse.get_pos()
            click = 0
        else:
            mouse = (0, 0)
    if state == 'player1' and mouse != (0, 0) and board[button(mouse)] == ' ':
        screen.blit(x, place(button(mouse)))
        state = 'player2'
        board[button(mouse)] = 'X'
    elif state == 'player2' and mouse != (0, 0) and board[button(mouse)] == ' ':
        screen.blit(o, place(button(mouse)))
        state = 'player1'
        board[button(mouse)] = 'O'
    if endgame.Winner(board, 'X'):
        winner = 'X'
        running = False
    elif endgame.Winner(board, 'O'):
        winner = 'O'
        running = False
    elif endgame.boardFull(board):
        winner = 'cat'
        running = False
    pg.display.update()
print(winner)
print(board)
pg.quit()




