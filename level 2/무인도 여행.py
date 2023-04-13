def bfs(i, j, r, c, visited, maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    deque = [[i,j]]
    visited[i][j] = 1
    cnt = int(maps[i][j])

    while deque:
        cx, cy = deque.pop(0)
        for i in range(4):
            # maps[cx][cy]의 상하좌우 체크
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 범위 선언 디테일 체크
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0 and maps[nx][ny] != "X":
                    deque.append([nx, ny])
                    visited[nx][ny] = 1
                    cnt += int(maps[nx][ny])
    
    return visited, cnt


def solution(maps):
    r, c = len(maps), len(maps[0])
    # 방문 확인용 2차원 리스트 생성
    visited = [[0]*c for _ in range(r)]
    answer = []
    
    for i in range(r):
        for j in range(c):
            if maps[i][j] != "X" and visited[i][j] == 0:
                visited, cnt = bfs(i, j, r, c, visited, maps)
                answer.append(cnt)
    
    # answer가 빈 값일 경우 예외처리
    return sorted(answer) if answer else [-1]
