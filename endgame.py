def boardFull(bo):
    count = 0
    for item in bo:
        if item != ' ':
            count += 1
    if count >= 9:
        return True
    return False

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