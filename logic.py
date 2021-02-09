import random

board = [1, ' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']


def RandomPos(let):
    for i in board:
        if i == ' ':
            i = let
            printBoard(board)
            break


def printBoard(board):
    print(" " + board[7] + " |" + " " + board[8] + " |" + " " + board[9] + " \n" +
          "___|___|___\n" +
          " " + board[4] + " |" + " " + board[5] + " |" + " " + board[6] + " \n" +
          "___|___|___\n" +
          " " + board[1] + " |" + " " + board[2] + " |" + " " + board[3] + " \n" +
          "   |   |   ")


def Winner(bo, let):
    if bo[1] == let and bo[2] == let and bo[3] == let:
        return True
    if bo[4] == let and bo[5] == let and bo[6] == let:
        return True
    if bo[7] == let and bo[8] == let and bo[9] == let:
        return True
    if bo[1] == let and bo[4] == let and bo[7] == let:
        return True
    if bo[2] == let and bo[5] == let and bo[8] == let:
        return True
    if bo[3] == let and bo[6] == let and bo[9] == let:
        return True
    if bo[1] == let and bo[5] == let and bo[9] == let:
        return True
    if bo[3] == let and bo[5] == let and bo[7] == let:
        return True
    return False


def placeRandom(ran):
    r = random.choice(ran)
    board[r] = 'O'


def compMove():
    NeedBMove = True
    NeedCMove = True
    NeedCenterMove = True
    NeedEMove = True
    posCor = []
    posEdg = []
    for i in range(1, 10):
        tb = board[:]
        if tb[i] == ' ':
            tb[i] = 'O'
            if Winner(tb, 'O'):
                board[i] = 'O'
                tb = board[:]
                NeedBMove = False
                NeedCMove = False
                NeedCenterMove = False
                NeedEmove = False
                break
    if NeedBMove == True:
        for i in range(1, 10):
            tb = board[:]
            if tb[i] == ' ':
                tb[i] = 'X'
                if Winner(tb, 'X'):
                    board[i] = 'O'
                    tb = board[:]
                    NeedBMove = False
                    NeedCMove = False
                    NeedCenterMove = False
                    NeedEmove = False
                    break
    if NeedCMove == True:
        # posCor = []
        if tb[7] == ' ':
            posCor.append(7)
        if tb[9] == ' ':
            posCor.append(9)
        if tb[1] == ' ':
            posCor.append(1)
        if tb[3] == ' ':
            posCor.append(3)
        if len(posCor) > 0:
            NeedCenterMove = False
            NeedEMove = False
            placeRandom(posCor)
    if NeedCenterMove == True:
        if tb[5] == ' ':
            board[5] = 'O'
            NeedCenterMove = False
            NeedEMove = False
    if NeedEMove == True:
        # posEdg = []
        if tb[8] == ' ':
            posEdg.append(7)
        if tb[6] == ' ':
            posEdg.append(9)
        if tb[4] == ' ':
            posEdg.append(1)
        if tb[2] == ' ':
            posEdg.append(3)
        if len(posCor) > 0:
            NeedEMove = False
            placeRandom(posEdg)


def PlayerMove():
    printBoard(board)
    move = input('Player turn (Use Numpad 1-9): ')
    board[int(move)] = 'X'


def BoardFull():
    for i in board:
        full = []
        if i == 'X' or i == 'Y':
            full.append(0)
    if len(full) >= 9:
        return True
    else:
        return False


def PlayerFirst():
    PlayerMove()
    if Winner(board, 'X'):
        print('Player wins')
        printBoard(board)
        return
    elif BoardFull():
        print("Board Full")
        printBoard(board)
        return
    compMove()
    printBoard(board)
    if Winner(board, 'O'):
        print("Computer wins")
        printBoard(board)
        return
    if BoardFull() == True:
        print("Board Full")
        printBoard(board)
        return
    PlayerFirst()


def CompFirst():
    compMove()
    if Winner(board, 'O'):
        print('Comp wins')
        printBoard(board)
        return 'CW'
    elif BoardFull():
        print("Board Full")
        printBoard(board)
        return 'BF'
    PlayerMove()
    printBoard(board)
    if Winner(board, 'X'):
        print("Player wins")
        printBoard(board)
        return 'PW'
    if BoardFull() == True:
        print("Board Full")
        printBoard(board)
        return 'BF'
    CompFirst()