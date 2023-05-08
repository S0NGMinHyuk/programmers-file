def solution(maps):
    # 방문 체크 + 이동 블럭 카운트용 2차원 리스트 생성
    visit = []
    temp = [0]*len(maps[0])
    for _ in range(len(maps)):
        visit.append(list(temp))
    
    dx = [0, 1, 0, -1]      # 상하좌우 이동 방향
    dy = [-1, 0, 1, 0]

    visit[0][0] = 1         # 시작 블록
    q = [[0, 0]]
    while q:
        y, x = q.pop(0)
        for i in range(4):  # 상하좌우 이동 가능한 블록 탐색
            nx = x + dx[i] ; ny = y + dy[i]
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps): 
                if maps[ny][nx] == 1 and visit[ny][nx] == 0:    # 이동할 수 있으면 q에 추가, visit 업데이트
                    visit[ny][nx] = visit[y][x] + 1
                    q.append([ny, nx])
    
    if visit[-1][-1]:       # 탐색을 마치고 목적지의 visit 값은 0 아니면 최단거리
        return visit[-1][-1]
    else:                   # 목적지의 visit 값이 0이면 갈 수 없다는 뜻
        return -1
