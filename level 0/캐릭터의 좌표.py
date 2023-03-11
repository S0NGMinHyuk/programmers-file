def move(direct, location, max):
    if direct == "up" and location[1] < max:
        location[1] += 1
    elif direct == "down" and location[1] > -max:
        location[1] -= 1
    elif direct == "right" and location[0] < max:
        location[0] += 1
    elif direct == "left" and location[0] > -max:
        location[0] -= 1
    return location



def solution(keyinput, board):
    maxWidth, maxHeight = board[0] // 2, board[1] //2
    location = [0, 0]

    for k in keyinput:
        if k in ["up", "down"]:
            location = move(k, location, maxHeight)
        else:
            location = move(k, location, maxWidth)

    return location
