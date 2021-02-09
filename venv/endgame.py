def boardFull(bo):
    count = 0
    for item in bo:
        if item != ' ':
            count += 1
    if count >= 9:
        return True
    return False


def winner(bo, let):
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


def compMove(board):
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
            if winner(tb, 'O'):
                #board[i] = 'O'
                tb = board[:]
                NeedBMove = False
                NeedCMove = False
                NeedCenterMove = False
                NeedEmove = False
                return i
    if NeedBMove == True:
        for i in range(1, 10):
            tb = board[:]
            if tb[i] == ' ':
                tb[i] = 'X'
                if winner(tb, 'X'):
                    #board[i] = 'O'
                    tb = board[:]
                    NeedBMove = False
                    NeedCMove = False
                    NeedCenterMove = False
                    NeedEmove = False
                    return i
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
            return placeRandom(posCor, board)
    if NeedCenterMove == True:
        if tb[5] == ' ':
            NeedCenterMove = False
            NeedEMove = False
            return 5
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
            return placeRandom(posEdg, board)


def placeRandom(posEdg, board):
    for i in posEdg:
        if board[i] == ' ':
            return i
