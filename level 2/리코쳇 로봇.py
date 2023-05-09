def solution(board):
    from collections import deque       # 큐 모듈 사용

    visit = [[0]*len(board[0]) for _ in range(len(board))]
    start, end = get_start_end(board)   # 시작 위치, 목표 위치 인덱스
    visit[start[0]][start[1]] = 1       # visit에 시작 위치 업데이트 (결과에서 1 빼기)
    q = deque([start])

    while q:                
        row, col = q.popleft()          # BFS 알고리즘 사용
        for idx in range(4):            # 상하좌우 이동 가능 위치 (ncol, nrow) 탐색
            ncol, nrow = get_next_spot(col, row, idx, board)

            if visit[nrow][ncol] == 0:  # 이동 후 위치가 처음 가는 위치면 visit 업데이트, q에 추가
                visit[nrow][ncol] = visit[row][col] + 1
                q.append([nrow, ncol])
    
    # visit 목표위치에 값이 있다면 리턴, 없다면 -1 리턴
    return visit[end[0]][end[1]] - 1 if visit[end[0]][end[1]] else -1


def get_start_end(board):       # board 리스트에서 시작위치(R)와 목표위치(G) 인덱스 반환 함수
    start, end = None, None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                start = [i, j]
            elif board[i][j] == "G":
                end = [i, j]
    return start, end


def get_next_spot(col, row, idx, board):            # 방향대로 이동한 위치 인덱스 반환 함수
    drow, dcol = [-1, 1, 0, 0], [0, 0, -1, 1]       # 상하좌우 이동

    while (0 <= col + dcol[idx] < len(board[0])     # 다음 위치가 인덱스 범위를 벗어나거나, 장애물일 경우 탈출
        and 0 <= row + drow[idx] < len(board)       # 그렇지 않다면(이동할 수 있다면) 계속 이동
        and board[row + drow[idx]][col + dcol[idx]]!= "D"):
        col += dcol[idx] ; row += drow[idx]
    
    return col, row
