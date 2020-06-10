
def can_put(bord, pos, num):
    y, x = pos
    if num in bord[y]:
        return False
    for i in range(len(bord)):
        if num == bord[i][x]:
            return False
    tri_y = y // 3
    tri_x = x // 3
    for i in range(3):
        for j in range(3):
            if num == bord[i + 3*tri_y][j + 3*tri_x]:
                return False
    return True

def rec_brute(bord):
    for y in range(0, 9):
        for x in range(0, 9):
            pos = (y, x)
            if bord[y][x] == 0:
                for num in range(1, 10):
                    if can_put(bord, pos, num):
                        bord[y][x] = num
                        fin_all, bord = rec_brute(bord)
                        if fin_all:
                            return True, bord
                        bord[y][x] = 0
                else:
                    return False, bord
    fin = True
    for line in range(9):
        if 0 in bord[line]:
            fin = False
    if fin:
        print('finished')
        for line in range(9):
            print(bord[line])
        return True, bord

