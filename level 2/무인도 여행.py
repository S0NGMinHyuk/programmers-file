def solution(maps):
    # 인덱스 오류 방지를 위한 maps 가공
    temp = []
    for i in maps:
        i = "X" + i + "X"
        temp.append(list(i))
    margin = ["X"] * (len(maps[0]) + 2)
    temp.insert(0, margin) ; temp.append(margin)
    maps = temp
    del(margin) ; del(temp)

    island = []
    for column in range(1, len(maps) - 1):
        for row in range(1, len(maps[0]) - 1):
            if maps[column][row] != "X":
                island.append(island_check(maps, column, row))
    
    return sorted(island) if island else [-1]



def island_check(maps, x, y):
    cnt = int(maps[x][y])
    maps[x][y] = "X"

    # 상하좌우 체크
    if left(maps, x, y):
        cnt += island_check(maps, x, y - 1)
    if right(maps, x, y):
        cnt += island_check(maps, x, y + 1)
    if up(maps, x, y):
        cnt += island_check(maps, x - 1, y)
    if down(maps, x, y):
        cnt += island_check(maps, x + 1, y)

    return cnt


def left(maps, x, y):
    return True if maps[x][y - 1] != "X" else False

def right(maps, x, y):
    return True if maps[x][y + 1] != "X" else False

def up(maps, x, y):
    return True if maps[x - 1][y] != "X" else False

def down(maps, x, y):
    return True if maps[x + 1][y] != "X" else False
