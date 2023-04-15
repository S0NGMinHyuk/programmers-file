def solution(maps):
    # s = 시작 인덱스, l = 레버 인덱스
    s, l= find_spot(maps)

    # 시작지점에서 레버까지의 최솟값
    go_to_lever = bfs(s, "L", maps)
    if go_to_lever == None:
        return -1
    
    # 레버에서 탈출지점까지의 최솟값
    go_to_exit = bfs(l, "E", maps)
    if go_to_exit == None:
        return -1
    
    return go_to_lever + go_to_exit


# 최솟값 계산 함수 (출발 인덱스, 도착지점 알파벳, maps)
def bfs(start, finish, maps):
    # 재방문 방지용 2차원 리스트 생성
    x, y = len(maps[0]), len(maps)
    visited = [[0] * x for _ in range(y)]

    dx = [1, 0 ,-1, 0]
    dy = [0, 1, 0, -1]

    # 선입선출 큐 사용
    q = [start]

    while q:
        ty, tx = q.pop(0)

        # 목표지점 도착 시 값 리턴
        if maps[ty][tx] == finish:
            return visited[ty][tx]
        
        # 상하좌우 탐색
        for i in range(4):
            cx = tx + dx[i]
            cy = ty + dy[i]
            
            # 인덱스 초과 방지 + 벽이 아닐 경우 + 첫 방문일 경우
            if 0 <= cx < x and 0 <= cy < y and maps[cy][cx] != "X" and visited[cy][cx] == 0:
                visited[cy][cx] = visited[ty][tx] + 1
                q.append([cy, cx])

    # 목표지점에 도착하지 못하는 경우, 즉 갇힌 경우
    return None


# 시작 위치, 레버 위치 탐색 함수
def find_spot(maps):
    ans = [0, 0]
    for i in range(len(maps)):
        if "S" in maps[i]:
            ans[0] = [i, maps[i].index("S")]
        if "L" in maps[i]:
            ans[1] = [i, maps[i].index("L")]
    return ans
