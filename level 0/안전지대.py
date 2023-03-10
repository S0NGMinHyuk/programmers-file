def solution(board):
    n = len(board)   # 행렬 길이

    bomb = []        # 폭탄 위치 인덱스
    for x in range(0, n):
        for y in range(0, n):
            if board[x][y] == 1:
                bomb.append([x, y])
    
    danger = []      # 위험 지역 인덱스
    for dot in bomb:
        x, y = dot[0], dot[1]
        for tx in range(x-1, x+2):
            if tx >= 0 and tx < n:    # 범위 초과 방지
                for ty in range(y-1, y+2):
                    if ty >= 0 and ty < n and [tx, ty] not in danger:
                        danger.append([tx, ty])
                    else:
                        continue
            else:
                continue
    
    return n**2 - len(danger)
