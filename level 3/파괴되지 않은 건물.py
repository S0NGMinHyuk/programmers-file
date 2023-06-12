def solution(board, skill):     # 정확성 통과, 효율성 실패
    bldg = len(board)*len(board[0])
    for i in range(len(skill)):
        type, *location, degree = skill[i]
        if type == 1:
            for row in range(location[0], location[2]+1):
                for col in range(location[1], location[3]+1):
                    if board[row][col] > 0 and (board[row][col]-degree) <= 0:
                        bldg -= 1
                    board[row][col] -= degree
        else: # type == 2:
            for row in range(location[0], location[2]+1):
                for col in range(location[1], location[3]+1):
                    if board[row][col] <= 0 and (board[row][col]+degree) > 0:
                        bldg += 1
                    board[row][col] += degree
    return bldg
