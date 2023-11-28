def solution(board, h, w):
    answer = 0
    n = len(board)
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]

    for i in range(4):
        if h+dh[i] >= 0 and h+dh[i] < n and w+dw[i] >= 0 and w+dw[i] < n:
            if board[h][w] == board[h+dh[i]][w+dw[i]]:
                answer += 1

    return answer
