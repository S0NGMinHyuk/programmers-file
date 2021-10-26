def solution(board):
    answer = 0                                                        # 가능한 정사각형의 길이
    for arr in board:                                                 # board의 행을 탐색하며
        if 1 in arr:                                                  # 행에 1이 있다면 answer를 1로 변경 후 탈출
            answer = 1
            break

    for height in  range(1, len(board)):                              # 0번째 행과 0번째 열은 스킵
        for row in range(1, len(board[0])):
            if board[height][row] == 1:                               # 목표 값이 1이라면 
                temp = min([board[height-1][row],                     # temp는 목표 값의 왼쪽, 위쪽, 왼쪽의 위쪽 값 중 최소값
                    board[height][row-1], board[height-1][row-1]])
                board[height][row] = temp + 1                         # 목표값을 temp+1 값으로 변경

                if board[height][row] > answer:                       # 목표값이 가능한 정사각형의 한 변의 길이이므로 
                    answer = board[height][row]                       # answer보다 크다면 answer값 변경

    return answer**2                                                  # 정사각형의 넓이 리턴


b = [[0], [1]]
print(solution(b)) # 정답 1